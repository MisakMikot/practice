from tkinter import filedialog
from PyQt5 import *
import sys

from PyQt5.QtCore import reset
from Main_ui import *
import os
import subprocess
import tkinter

root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
root.withdraw()
mode = None


def slotConnect():
    MainWindowUi.adb_s_btn_excute.clicked.connect(lambda: sexecute())
    MainWindowUi.pushButton.clicked.connect(lambda: reboot())
    MainWindowUi.pushButton_4.clicked.connect(lambda: devices())
    MainWindowUi.pushButton_6.clicked.connect(lambda: listAllPacks())
    MainWindowUi.pushButton_7.clicked.connect(lambda: listSysPacks())
    MainWindowUi.pushButton_12.clicked.connect(lambda: getSerialNo())
    MainWindowUi.pushButton_11.clicked.connect(lambda: getLog())
    MainWindowUi.pushButton_13.clicked.connect(lambda: getModule())
    MainWindowUi.pushButton_14.clicked.connect(lambda: getAndroid())
    MainWindowUi.pushButton_15.clicked.connect(lambda: getResolution())
    MainWindowUi.pushButton_2.clicked.connect(lambda: shutdown())
    MainWindowUi.pushButton_3.clicked.connect(lambda: installApk())
    MainWindowUi.pushButton_16.clicked.connect(lambda: getScreenShot())
    MainWindowUi.pushButton_5.clicked.connect(lambda: uninstallApp())
    MainWindowUi.adb_a_btn_confirm.clicked.connect(lambda: parmOk())
    MainWindowUi.pushButton_8.clicked.connect(lambda: clearPackData())
    MainWindowUi.install_wechat.clicked.connect(lambda: wechat())
    MainWindowUi.pushButton_9.clicked.connect(lambda: startApp())
    MainWindowUi.pushButton_10.clicked.connect(lambda: stopApp())


def stopApp():
    global mode
    mode = 'stop'
    MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('输入包名')


def startApp():
    global mode
    mode = 'start'
    MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('输入包名')


def clearPackData():
    global mode
    mode = 'clear'
    MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('输入包名')


def wechat():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb install C:\\Users\\wangly\\OneDrive\\pythons\\ADBTool\\data\\apks\\weixin.apk'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def parmOk():
    parm = MainWindowUi.adb_a_lineedit_parm.text()
    if not mode == None:
        if not parm == '':
            if mode == 'unins':
                cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb uninstall '+parm
                pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                bresult = pi.stdout.read()
                result = bresult.decode('utf-8')
                MainWindowUi.textEdit.setText(result)
                MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('参数输入框')
                return
            elif mode == 'clear':
                cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell pm clear '+parm
                pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                bresult = pi.stdout.read()
                result = bresult.decode('utf-8')
                MainWindowUi.textEdit.setText(result)
                MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('参数输入框')
                return
            elif mode == 'start':
                cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell am start -n '+parm
                pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                bresult = pi.stdout.read()
                result = bresult.decode('utf-8')
                MainWindowUi.textEdit.setText(result)
                MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('参数输入框')
                return
            elif mode == 'stop':
                cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell am force-stop '+parm
                pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                bresult = pi.stdout.read()
                result = bresult.decode('utf-8')
                MainWindowUi.textEdit.setText(result)
                MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('参数输入框')
                return
        MainWindowUi.textEdit.setText('参数不能为空')
    MainWindowUi.textEdit.setText('未选择模式')


def uninstallApp():
    global mode
    mode = 'unins'
    MainWindowUi.adb_a_lineedit_parm.setPlaceholderText('输入包名')


def getScreenShot():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell screencap -p /sdcard/screen.png'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)
    Savepath = filedialog.asksaveasfilename(
        title=u'保存图片', filetypes=[('PNG图像', '.png')], defaultextension='png')
    if not Savepath == '':
        cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb pull /sdcard/screen.png '+Savepath
        pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        bresult = pi.stdout.read()
        result = bresult.decode('utf-8')
        MainWindowUi.textEdit.setText(result)


def installApk():
    Apkpath = filedialog.askopenfilename(title=u'安装Apk', filetypes=[
                                         ('Android应用程序包', '.apk')], defaultextension='apk')
    if not Apkpath == '':
        cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb install '+Apkpath
        pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        bresult = pi.stdout.read()
        result = bresult.decode('utf-8')
        MainWindowUi.textEdit.setText(result)


def shutdown():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell reboot -p'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def getResolution():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell wm size'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def getAndroid():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell getprop ro.build.version.release'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText('Android '+result)


def getModule():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell getprop ro.product.model'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def getLog():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb logcat'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def getSerialNo():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb get-serialno'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def listSysPacks():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell pm list packages -s'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def listAllPacks():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb shell pm list packages'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def sexecute():
    precmd = MainWindowUi.adb_s_lineedit_cmdbox.text()
    if precmd == '':
        MainWindowUi.adb_s_textedit_result.setText('空白命令！')
        return
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb '+precmd
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.adb_s_textedit_result.setText(result)


def reboot():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb reboot'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


def devices():
    cmd = 'C:\\Users\wangly\OneDrive\pythons\ADBTool\data\\adb devices'
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    bresult = pi.stdout.read()
    result = bresult.decode('utf-8')
    MainWindowUi.textEdit.setText(result)


if __name__ == '__main__':  # 程序主方法
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    MainWindowUi = Ui_MainWindow()
    MainWindowUi.setupUi(Main)
    Main.show()
    slotConnect()
    sys.exit(app.exec_())
