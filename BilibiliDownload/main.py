import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QBrush, QColor, QIcon, QMovie, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QDialog, QFileDialog, QProgressBar

import bl_download
import cookies
from download import *

'''
Cookies界面
'''
class CookieDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = cookies.Ui_CookieDialog()
        self.ui.setupUi(self)
        self.ui.cancel_btn.released.connect(self.close_cookie)

    def close_cookie(self):
        self.close()

'''
主界面
'''
class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = bl_download.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化Cookie界面
        self.cookie_window = CookieDialog()
        self.cookie_window.setWindowIcon(QIcon('logo.ico'))
        self.cookie_window.ui.ok_btn.released.connect(self.setCookie)

        # 连接信号和槽
        self.ui.download_all_btn.released.connect(self.download_all)
        self.ui.analy_btn.released.connect(self.analy)
        self.ui.savepath_btn.released.connect(self.save_path_btn_slot)
        self.ui.set_cookies_btn.released.connect(self.showCookieWin)

        # 设置表格列数、宽度和表头
        self.ui.downloadlink_table.setColumnCount(3)
        header_list = ['名称', '进度', '下载']
        self.ui.downloadlink_table.setHorizontalHeaderLabels(header_list)
        self.ui.downloadlink_table.setColumnWidth(0, 300)
        self.ui.downloadlink_table.setColumnWidth(1, 200)
        self.ui.downloadlink_table.setColumnWidth(2, 50)

        # 将下载所有按钮置灰
        self.ui.download_all_btn.setDisabled(True)

        # 设置状态栏和解析进度条
        self.statusBar().showMessage('就绪')
        self.progressBar = QProgressBar()
        self.progressBar.hide()
        self.progressBar.setRange(0, 100)
        self.statusBar().addPermanentWidget(self.progressBar)

        # 初始化保存路径、Cookie和下载队列
        current_path = os.getcwd()
        default_download_path = current_path + '\Bilibili_Download'
        self.ui.savepath_LineEdit.setText(default_download_path)
        self.cookie = ''
        self.download_queue = []

    '''
        显示设置Cookie界面
    '''
    def showCookieWin(self):
        self.cookie_window.show()

    '''
        设置大会员Cookie
    '''
    def setCookie(self):
        self.cookie = self.cookie_window.ui.cookie_textEdit.toPlainText()
        self.cookie_window.close()

    '''
        回调函数：保存路径按钮
    '''
    def save_path_btn_slot(self):
        # 获取初始路径，如果初始路径不存在，则使用当前路径
        def_path = self.ui.savepath_LineEdit.text()
        if not os.path.exists(def_path):
            def_path = os.getcwd()
        # 打开路径选择对话框
        save_path = QFileDialog.getExistingDirectory(self, '选择保存路径', def_path)
        if save_path != '':
            self.ui.savepath_LineEdit.setText(save_path)

    '''
       下载全部按钮的回调函数，点击下载按钮时执行
       功能：下载所有视频
       返回值：无
    '''
    def download_all(self):
        # 获取视频数量，清空下载队列
        row_cnt = self.ui.downloadlink_table.rowCount()
        self.download_queue = []

        # 切换’下载全部‘和’取消下载全部‘
        btn_text = self.ui.download_all_btn.text()
        if btn_text == '取消下载全部':
            self.ui.download_all_btn.setText('下载全部')
            for i in range(row_cnt):
                dl_btn = self.ui.downloadlink_table.cellWidget(i, 2)
                if dl_btn.text() == '取消':
                    dl_btn.click()
                else:
                    text_item = QtWidgets.QTableWidgetItem()
                    text_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    text_item.setText('等待下载')
                    self.ui.downloadlink_table.setItem(i, 1, text_item)
        else:
            self.ui.download_all_btn.setText('取消下载全部')
            for i in range(row_cnt):
                # 如果下载数量大于5，将剩余的加入下载队列，等其他视频下载完成再开始下载
                if i >= 5:
                    name = self.ui.downloadlink_table.item(i, 0).text()
                    if name.find('需要大会员') != -1:
                        continue
                    self.download_queue.append(i)
                    self.ui.downloadlink_table.removeCellWidget(i, 1)
                    text_item = QtWidgets.QTableWidgetItem()
                    text_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    text_item.setText('下载队列中')
                    self.ui.downloadlink_table.setItem(i, 1, text_item)
                else:
                    dl_btn = self.ui.downloadlink_table.cellWidget(i, 2)
                    dl_btn.click()

    '''
       槽函数：更新下载进度条
       progress：0-100表示下载视频进度，100-200表示下载音频进度 -1表示下载出错，-2表示取消下载
       row：视频链接所在的行，从0开始
    '''
    def upd_progress(self, progress, row):
        # 更新进度条
        pro_bar = self.ui.downloadlink_table.cellWidget(row, 1)
        pro_bar.setValue(progress)

        # 如果下载失败或者下载完成，移除进度条，并显示下载状态
        if progress == -1 or progress == 200 or progress == -2:
            self.ui.downloadlink_table.removeCellWidget(row, 1)
            text_item = QtWidgets.QTableWidgetItem()
            text_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            if progress == -1:
                text_item.setText('下载失败')
            elif progress == -2:
                text_item.setText('取消下载')
            else:
                text_item.setText('下载完成')
            self.ui.downloadlink_table.setItem(row, 1, text_item)

            # 清除缓存文件
            #file_name = self.ui.downloadlink_table.item(row, 0)
            #correct_file_name(file_name)
            #os.remove('./cache/' + file_name + '.mp3')
            #os.remove('./cache/' + file_name + '.mp4')

            # 更新下载按钮
            btn = self.ui.downloadlink_table.cellWidget(row, 2)
            btn.disconnect()
            btn.setText('下载')
            btn.released.connect(self.download)

            # 从下载队列中取出下一个
            if len(self.download_queue) != 0:
                dl_btn = self.ui.downloadlink_table.cellWidget(self.download_queue.pop(0), 2)
                dl_btn.click()

    '''
        回调函数：下载按钮
    '''
    def download(self):
        dl_btn = self.sender()
        if not dl_btn:
            return

        # 获取按钮所在行
        row = self.ui.downloadlink_table.indexAt(dl_btn.pos()).row()

        # 添加进度条
        pro_bar = QtWidgets.QProgressBar()
        pro_bar.setRange(0, 200)
        pro_bar.setValue(0)
        self.ui.downloadlink_table.setCellWidget(row, 1, pro_bar)

        # 设置取消按钮
        dl_btn.setText('取消')
        dl_btn.disconnect()

        # 获取选中视频的链接
        url = self.ui.downloadlink_table.item(row, 0).data(QtCore.Qt.UserRole)

        # 创建并启动下载线程
        download_thread = DownloadThread(url, row)
        download_thread.download_sig.connect(self.upd_progress)
        download_thread.setCookie(self.cookie)
        download_thread.set_save_path(self.ui.savepath_LineEdit.text())
        dl_btn.released.connect(download_thread.cancel_slot)
        download_thread.start()
        time.sleep(0.01)

    '''
    回调函数：解析按钮
    '''
    def analy(self):
        # 获取用户输入的链接
        org_url = self.ui.downloadlink_LineEdit.text()
        if len(org_url) == 0:
            QMessageBox.warning(self, '无效的链接', '无效的链接', QMessageBox.Close)
            return

        # 设置状态
        self.ui.downloadlink_table.setRowCount(0)
        self.statusBar().showMessage('正在解析...')
        self.progressBar.show()

        # 创建并启动解析线程
        analy_thread = AnalyThread(org_url)
        analy_thread.analy_sig.connect(self.analy_slot)
        analy_thread.start()
        time.sleep(0.01)


    '''
        槽函数：链接解析
    '''
    def analy_slot(self, url_dict, progress):
        if progress == -1:
            QMessageBox.warning(self, '解析失败', '解析失败', QMessageBox.Close)
            self.statusBar().showMessage('解析失败')
            self.ui.download_all_btn.setDisabled(True)
            self.progressBar.hide()
            return
        elif progress == 100:
            self.ui.download_all_btn.setDisabled(False)
            self.statusBar().showMessage('解析成功')
            self.progressBar.hide()

        # 更新进度条
        self.progressBar.setValue(progress)
        # 在表格末尾加入一行
        row_cnt = self.ui.downloadlink_table.rowCount()
        self.ui.downloadlink_table.insertRow(row_cnt)

        # 添加下载视频标题
        need_big_member = 1 if url_dict['title'].find('需要大会员') != -1 else 0
        analy_failed = 1 if url_dict['title'].find('解析失败') != -1 else 0
        item = QtWidgets.QTableWidgetItem(url_dict['title'])
        item.setData(QtCore.Qt.UserRole, QVariant(url_dict))
        if need_big_member or analy_failed:
            item.setForeground(QBrush(QColor('red')))
        self.ui.downloadlink_table.setItem(row_cnt, 0, item)
        # 添加等待下载状态
        text_item = QtWidgets.QTableWidgetItem('无法下载' if need_big_member or analy_failed else '等待下载')
        text_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.ui.downloadlink_table.setItem(row_cnt, 1, text_item)
        # 添加下载按钮
        dl_btn = QtWidgets.QPushButton('下载')
        dl_btn.released.connect(self.download)
        if need_big_member or analy_failed:
            dl_btn.setEnabled(False)
        self.ui.downloadlink_table.setCellWidget(row_cnt, 2, dl_btn)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MyMainWindow()
    myDlg.setWindowIcon(QIcon('logo.ico'))
    myDlg.show()
    sys.exit(myapp.exec_())
