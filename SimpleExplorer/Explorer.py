import os
import shutil
import socket
import sys
import threading
import hashlib

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileSystemModel, QWidget, QInputDialog, QLineEdit, QApplication

from form_ui import Ui_Widget as uwg


class NewWidget(QWidget):
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self, "Exit", "Do you want to exit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if (result == QtWidgets.QMessageBox.Yes):
            event.accept()
            sys.exit()
        else:
            event.ignore()


class Ui_calcHash(object):
    def setupUi(self, calcHash):
        calcHash.setObjectName("calcHash")
        calcHash.resize(135, 188)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calcHash.sizePolicy().hasHeightForWidth())
        calcHash.setSizePolicy(sizePolicy)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(calcHash)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 150, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.radioButton = QtWidgets.QRadioButton(calcHash)
        self.radioButton.setGeometry(QtCore.QRect(10, 0, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(calcHash)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(calcHash)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 80, 91, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(calcHash)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 120, 91, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setObjectName("radioButton_4")
        self.mode = None

        self.retranslateUi(calcHash)
        QtCore.QMetaObject.connectSlotsByName(calcHash)

    def retranslateUi(self, calcHash):
        _translate = QtCore.QCoreApplication.translate
        calcHash.setWindowTitle(_translate("calcHash", "Form"))
        self.commandLinkButton.setText(_translate("calcHash", "CALCULATE"))
        self.radioButton.setText(_translate("calcHash", "MD5"))
        self.radioButton_2.setText(_translate("calcHash", "SHA1"))
        self.radioButton_3.setText(_translate("calcHash", "SHA128"))
        self.radioButton_4.setText(_translate("calcHash", "SHA256"))
        self.commandLinkButton.clicked.connect(self.calc)

    def calc(self):
        if self.radioButton.isChecked():
            self.mode = "md5"
        elif self.radioButton_2.isChecked():
            self.mode = "sha1"
        elif self.radioButton_3.isChecked():
            self.mode = "sha128"
        elif self.radioButton_4.isChecked():
            self.mode = "sha256"
        dlg.hide()


class Ui_Widget(QtWidgets.QWidget, uwg):

    def slotConnection(self):
        self.treeView.doubleClicked.connect(lambda: self.slotDoubleClicked())
        self.Delete.clicked.connect(lambda: self.slotDelete())
        self.Copy.clicked.connect(lambda: self.slotCopy())
        self.Paste.clicked.connect(lambda: self.slotPaste())
        self.Rename.clicked.connect(lambda: self.slotRename())
        self.copyPath.clicked.connect(lambda: self.slotCopyPath())
        self.Notepad.clicked.connect(lambda: self.slotNotepad())
        self.calcHash.clicked.connect(lambda: self.slotCalcHash())

    def fcalcHash(self, path):
        lenth = os.path.getsize(path)
        progress = 0
        block_size = 4096
        hash = None
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.label.setText("")
        while True:
            mode = dlgUi.mode
            if mode == "md5":
                hash = hashlib.md5()
                with open(path, "rb") as f:
                    for byte_block in iter(lambda: f.read(block_size), b""):
                        print(1)
                        hash.update(byte_block)
                        print(2)
                        progress += block_size
                        print(3)
                        percent = int(progress / lenth * 100)
                        print(4)
                        self.progressBar.setValue(percent)
                        print(5)
                        self.label.setText("已完成MD5计算：{} MB / {} MB".format(round(progress / 1024 / 1024, 1), round(lenth / 1024 / 1024, 1)))
                        print(6)
                        print(progress, lenth)
                        if progress >= lenth:
                            print(7)
                            self.label.setText("MD5计算完成")
                            print(8)
                            _ = QMessageBox.information(self, "信息", "MD5计算完成")
                            print(9)
                            break
            elif mode == "sha1":
                hash = hashlib.sha1()
                with open(path, "rb") as f:
                    for byte_block in iter(lambda: f.read(block_size), b""):
                        hash.update(byte_block)
                        progress += block_size
                        percent = int(progress / lenth * 100)
                        self.progressBar.setValue(percent)
                        self.label.setText("已完成SHA1计算：{} MB / {} MB".format(round(progress / 1024 / 1024, 1), round(lenth / 1024 / 1024, 1)))
                        if progress >= lenth:
                            self.label.setText("SHA1计算完成")
                            QMessageBox.information(self, "信息", "SHA1计算完成")
                            break
            elif mode == "sha128":
                hash = hashlib.sha1()
                with open(path, "rb") as f:
                    for byte_block in iter(lambda: f.read(block_size), b""):
                        hash.update(byte_block)
                        progress += block_size
                        percent = int(progress / lenth * 100)
                        self.progressBar.setValue(percent)
                        self.label.setText("已完成SHA128计算：{} MB / {} MB".format(round(progress / 1024 / 1024, 1), round(lenth / 1024 / 1024, 1)))
                        if progress >= lenth:
                            self.label.setText("SHA128计算完成")
                            QMessageBox.information(self, "信息", "SHA128计算完成")
                            break
            elif mode == "sha256":
                hash = hashlib.sha256()
                with open(path, "rb") as f:
                    for byte_block in iter(lambda: f.read(block_size), b""):
                        hash.update(byte_block)
                        progress += block_size
                        percent = int(progress / lenth * 100)
                        self.progressBar.setValue(percent)
                        self.label.setText("已完成SHA256计算：{} MB / {} MB".format(round(progress / 1024 / 1024, 1), round(lenth / 1024 / 1024, 1)))
                        if progress >= lenth:
                            self.label.setText("SHA256计算完成")
                            QMessageBox.information(self, "信息", "SHA256计算完成")
                            break
            else:
                pass

    def slotCalcHash(self):
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        if os.path.isfile(path):
            dlg.show()
            t = threading.Thread(target=self.fcalcHash, args=(path,))
            t.start()
        else:
            QMessageBox.information(self, "提示", "请选择文件")

    def slotNotepad(self):
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index).replace("\\", "/")
        if os.path.isfile(path):
            os.popen("notepad.exe " + path)
        else:
            QMessageBox.information(self, "提示", "请选择文件")

    def slotCopyPath(self):
        '''
        复制文件路径
        :return:
        '''
        clipboard = QApplication.clipboard()
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index)
        clipboard.setText(path)
        QMessageBox.information(self, "提示", "已复制路径到剪贴板")

    def getString(self, tip, title, foldername):
        string = QInputDialog.getText(self, title, tip, QLineEdit.Normal, foldername)
        return string[0]

    def rename(self, path, dst):
        os.rename(path, dst)
        return

    def slotRename(self):
        index = self.treeView.currentIndex()
        path = self.treeView.model().filePath(index).replace("\\", "/")
        if os.path.isdir(path):
            foldername = path.split("/")[-1]
            folders = path.split("/")
            dst = self.getString("请输入新的文件夹名称", "重命名", foldername)
            if dst == "":
                return
            folders.pop(-1)
            folders.append(dst)
            dst = "/".join(folders)
            self.rename(path, dst)
            return
        elif os.path.isfile(path):
            index = self.treeView.currentIndex()
            path = self.treeView.model().filePath(index).replace("\\", "/")
            filename = path.split("/")[-1]
            dst = self.getString("请输入新的文件名称", "重命名", filename)
            if dst == "":
                return
            folders = path.split("/")
            folders.pop(-1)
            folders.append(dst)
            dst = "/".join(folders)
            self.rename(path, dst)
            return

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
    dlg = QWidget()
    dlgUi = Ui_calcHash()
    dlgUi.setupUi(dlg)
    MainWindowUi.main()
    sys.exit(app.exec_())
