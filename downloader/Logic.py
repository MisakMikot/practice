from Main_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import requests
import time
import platform
from tkinter import *
import tkinter.messagebox
tkint = Tk()
tkint.withdraw()

def slotConnection():
    MainWindowUi.pushButton.clicked.connect(lambda:startdl())
    MainWindowUi.pushButton_2.clicked.connect(lambda:openDir())
    MainWindowUi.action.triggered.connect(lambda:openDir())
    MainWindowUi.action_3.triggered.connect(lambda:quit())
    MainWindowUi.action_4.triggered.connect(lambda:about())
    MainWindowUi.action_5.triggered.connect(lambda:howUse())

def howUse():
    QDialog = QtWidgets.QMessageBox.information(Main, '使用说明', '把下载链接放在输入框\n注意：链接要带有文件名！！！\n然后点开始下载\n下好了以后点打开目录就可以了\n\n\n不要作死去放无效的链接，会崩！')

def about():
    QDialog = QtWidgets.QMessageBox.information(Main, '关于', '卢本伟下载器\n制作  By LuoyuXQ\n遵循CC BY SA 协议')

def quit():
    sys.exit()

def openConfig():
    pass

def openDir():
    os.startfile('downloads')
    MainWindowUi.pushButton_2.setDisabled(True)
    MainWindowUi.action.setDisabled(True)

def startdl():
    if os.path.exists('downloads') == False:
        os.mkdir('downloads')
    MainWindowUi.pushButton_2.setDisabled(True)
    MainWindowUi.lineEdit.setDisabled(True)
    url = MainWindowUi.lineEdit.text()
    filenames = url.split('/')
    filename = filenames[-1]
    headers = 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    response =  requests.get(url,stream=True)
    size = 0
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    fsize_mb = content_size / chunk_size / 1024
    fsize_kb = content_size / chunk_size
    try:
        if response.status_code == 200:
            QDialog = QtWidgets.QMessageBox.information(Main, '提示', '按OK开始下载！\n文件大小：{size:.2f} MB\n下载进程不可逆！'.format(size = content_size / chunk_size / 1024))
            start = time.time()
            with open('downloads\\'+filename,'wb') as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    MainWindowUi.progressBar.setValue(round(size / content_size * 100))
                    #MainWindowUi.lcdNumber.display(round(size / content_size * 100))
        elif response.status_code == 404:
            QDialog = QtWidgets.QMessageBox.warning(Main,'警告','服务器返回：\n404 Not Found')
            return
        end = time.time()
        allt = end - start
        time_mb = fsize_mb / allt
        time_kb = fsize_kb / allt
        MainWindowUi.progressBar.setValue(0)
        MainWindowUi.pushButton_2.setDisabled(False)
        MainWindowUi.action.setDisabled(False)
        MainWindowUi.lineEdit.setDisabled(False)
        #MainWindowUi.lcdNumber.display(0)
        QDialog = QtWidgets.QMessageBox.information(Main, '提示', f'下载完成！\n总用时{allt}秒\n平均速度为：\n{round(time_mb,2)} MB/S\n{round(time_kb)} KB/s')
    except Exception as ex:
        QDialog = QtWidgets.QMessageBox.warning(Main, '错误', str(ex))

if __name__ == '__main__':  # 程序主方法
    systype = platform.system()
    if not systype == 'Windows':
        tkinter.messagebox.showerror('严重错误','此应用只能在Windows系统下运行！')
        sys.exit()
    #elif systype == 'Windows':
        #print('lbwnb')
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    MainWindowUi = Ui_MainWindow()
    MainWindowUi.setupUi(Main)
    Main.show()
    slotConnection()
    sys.exit(app.exec_())
