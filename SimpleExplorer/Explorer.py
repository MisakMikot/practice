import os
import shutil
import socket
import sys
import threading

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileSystemModel, QWidget, QInputDialog, QLineEdit

from form_ui import Ui_Widget as uwg

copypath = ""
path = ""
ok = 0
lenth = 0


class NewWidget(QWidget):
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self, "Exit", "Do you want to exit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if (result == QtWidgets.QMessageBox.Yes):
            event.accept()
            sys.exit()
        else:
            event.ignore()


class Ui_Widget(QtWidgets.QWidget, uwg):

    def slotConnection(self):
        self.treeView.doubleClicked.connect(lambda: self.slotDoubleClicked())
        self.Delete.clicked.connect(lambda: self.slotDelete())
        self.Copy.clicked.connect(lambda: self.slotCopy())
        self.Paste.clicked.connect(lambda: self.slotPaste())
        self.Rename.clicked.connect(lambda: self.slotRename())

    def getString(self, tip, title, foldername):
        print(1)
        string = QInputDialog.getText(self, title, tip, QLineEdit.setText(foldername), "")
        print(string)
        return string

    def rename(self, path, dst):
        os.rename(path, dst)

    def slotRename(self):
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index).replace("\\", "/")
        if os.path.isdir(path):
            foldername = path.split("/")[-1]
            path = path + "/"
            dst = self.getString("请输入新的文件夹名称", "重命名", foldername)
            if dst == "":
                return
            dst = path + dst
            print("from: {} to: {}".format(path, dst))
        elif os.path.isfile(path):
            path = os.path.basename(path)

    def copy_dir(self, src_path, target_path):
        global lenth
        ok = 0
        src_name = os.path.basename(src_path)
        target_path = os.path.join(target_path, src_name).replace("\\", "/")
        if not os.path.exists(target_path):
            os.mkdir(target_path)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(0)
        self.progressBar_2.show()
        self.label_2.show()
        files = []
        for root, dirs, files in os.walk(src_path):
            files = files
        lenth = len(files)
        print(lenth)
        ok = 0
        if os.path.isdir(src_path) and os.path.isdir(target_path):
            filelist_src = os.listdir(src_path)
            for file in filelist_src:
                path = os.path.join(os.path.abspath(src_path), file)
                if os.path.isdir(path):
                    path1 = os.path.join(os.path.abspath(target_path), file)
                    if not os.path.exists(path1):
                        os.mkdir(path1)
                    self.copy_dir(path, path1)
                else:
                    path1 = os.path.join(target_path, file)
                    filesize = os.path.getsize(path)
                    with open(path, 'rb') as read_stream:
                        contents = read_stream.read()
                        path1 = os.path.join(target_path, file)
                        with open(path1, 'wb') as write_stream:
                            print("正在复制文件：" + path)
                            t = threading.Thread(target=self.check_file, args=(path1, filesize))
                            t.start()
                            write_stream.write(contents)
                            ok += 1
                            percent = ok / lenth * 100
                            self.progressBar_2.setValue(round(percent))
                            print("复制完成:" + path)
        return

    def check_file(self, path, filesize):
        print("check_start" + path)
        self.progressBar.setMaximum(100)
        self.label.setText("")
        while True:
            now_size = os.path.getsize(path)
            percent = now_size / filesize * 100
            self.progressBar.setValue(round(percent))
            self.label.setText(
                "已完成 {} MB / {} MB".format(round(now_size / 1024 / 1024, 2), round(filesize / 1024 / 1024, 2)))
            print("已完成 {} MB / {} MB".format(round(now_size / 1024 / 1024, 2), round(filesize / 1024 / 1024, 2)))
            if now_size == filesize:
                print("check_done" + path)
                return

    def copyFile(self, cpath, copypath):
        shutil.copy(copypath, cpath)

    def copyCheck(self, filesize, cpath, copypath, dirmode=False):
        t = threading.Thread(target=self.copyFile, kwargs={"cpath": cpath, "copypath": copypath})
        t.start()
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        while True:
            if os.path.exists(cpath):
                if os.path.isfile(cpath):
                    oksize = os.path.getsize(cpath)
                    percent = oksize / filesize * 100
                    self.progressBar.setValue(int(percent))
                    self.label.setText(
                        "已完成: {} MB / {} MB".format(round(oksize / 1024 / 1024), round(filesize / 1024 / 1024)))
                    if oksize == filesize:
                        self.progressBar.setValue(100)
                        self.label.setText("复制完成")
                        if dirmode == False:
                            pass
                        else:
                            global ok
                            ok += 1
                            break
                        break

    def slotPaste(self):
        '''
        粘贴文件或文件夹
        :return:
        '''
        index = self.treeView.currentIndex()
        cpath = self.treeView.model().filePath(index)
        global copypath
        if copypath == "":
            return
        try:
            if os.path.isdir(copypath):
                t = threading.Thread(target=self.copy_dir, kwargs={"target_path": cpath, "src_path": copypath})
                t.start()
            elif os.path.isfile(copypath):
                filename = os.path.basename(copypath)
                cpath = cpath + "/" + filename
                filesize = os.path.getsize(copypath)
                t = threading.Thread(target=self.copyCheck,
                                     kwargs={"cpath": cpath, "filesize": filesize, "copypath": copypath})
                t.start()
        except Exception as e:
            QMessageBox.information(self.treeView, "错误", "无法粘贴文件或文件夹: \n" + str(e))

    def slotCopy(self):
        '''
        复制文件或文件夹
        :return:
        '''
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        global copypath
        copypath = path

    def slotDelete(self):
        '''
        删除选中文件或文件夹
        :return:
        '''
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        if os.path.isdir(path):
            reply = QMessageBox.question(self.treeView, '警告', '是否删除文件夹？\n' + path,
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    shutil.rmtree(path)
                except Exception as e:
                    QMessageBox.information(self.treeView, "错误", "无法删除文件夹: \n" + str(e))
            else:
                return

        else:
            reply = QMessageBox.question(self.treeView, '警告', '是否删除文件？\n' + path,
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    os.remove(path)
                except Exception as e:
                    QMessageBox.information(self.treeView, "错误", "无法删除文件: \n" + str(e))
            else:
                return

    def slotDoubleClicked(self):
        '''
        :return:
        '''
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        try:
            if os.path.isdir(path):
                pass
            else:
                os.system(path)
        except:
            QMessageBox.information(self.treeView, "Error", "Can't open file")

    def main(self):
        self.slotConnection()
        self.label_2.hide()
        self.progressBar_2.hide()
        model = QFileSystemModel()
        model.setRootPath(QDir.rootPath())
        self.treeView.setModel(model)
        PCName = socket.gethostname()


if __name__ == '__main__':  # 程序主方法
    app = QtWidgets.QApplication(sys.argv)
    Main = NewWidget()
    MainWindowUi = Ui_Widget()
    MainWindowUi.setupUi(Main)
    Main.show()
    MainWindowUi.main()
    sys.exit(app.exec_())
