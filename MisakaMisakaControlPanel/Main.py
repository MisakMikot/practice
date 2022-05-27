# testtoken eb15717586f7d01a7245775a8e35fc119b08a62d029d9f7df09596f85c851c09
# maintoken f67a9b9982340e772cec297fd3c1fcc699d7e60e6b800025faa28b34ebfccab9
# 潘潘 17717609895
import json
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox as Msg

from Main_ui import Ui_MainWindow


def slotConnection():
    '''
    信号槽链接
    '''
    MainWindowUi.sendMsg.clicked.connect(lambda: sendMsg())


def sendMsg():
    '''
    用来发送消息
    '''
    chkState = MainWindowUi.isAtAll.checkState()
    if chkState == 0:
        isAtAll = "false"
    else:
        isAtAll = "true"
    content = MainWindowUi.content.toPlainText()
    atMobiles = MainWindowUi.atMobiles.text()
    if not atMobiles == '':
        try:
            int(atMobiles)
        except ValueError:
            Msg.warning(Main, '警告', '手机号只能为整数!')
            return
    unFormatData = {"at": {"atMobiles":[atMobiles],"atUserIds":[""],"isAtAll": isAtAll},"text": {"content":content+"\n御坂御坂如是说"},"msgtype":"text"}
    data = json.dumps(unFormatData, indent=2, sort_keys=True, ensure_ascii=False)
    tokens = MainWindowUi.robotToken.text()
    if tokens == '':
        Msg.warning(Main, '警告', '空的TOKEN!')
        return
    headers = {"content-type": "application/json"}
    url = "https://oapi.dingtalk.com/robot/send?access_token="+tokens
    response = requests.post(url, data=data.encode('utf-8'), headers=headers)
    errcode = response.text
    print(errcode)
    if errcode == '{"errcode":300001,"errmsg":"token is not exist"}':
        Msg.warning(Main, '警告', 'TOKEN不存在!')
    elif errcode == '{"errcode":310000,"errmsg":"keywords not in content, more: [https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq]"}':
        Msg.warning(Main, '警告', '内容中缺少关键词！')



if __name__ == '__main__':  # 程序主方法
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    MainWindowUi = Ui_MainWindow()
    MainWindowUi.setupUi(Main)
    Main.show()
    slotConnection()
    sys.exit(app.exec_())
