# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\practice\WiFiCrack\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_dict = QtWidgets.QWidget()
        self.tab_dict.setObjectName("tab_dict")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_dict)
        self.tabWidget_2.setGeometry(QtCore.QRect(-4, -1, 791, 531))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_dict_crack = QtWidgets.QWidget()
        self.tab_dict_crack.setObjectName("tab_dict_crack")
        self.le_dictadd = QtWidgets.QLineEdit(self.tab_dict_crack)
        self.le_dictadd.setGeometry(QtCore.QRect(0, 0, 421, 31))
        self.le_dictadd.setObjectName("le_dictadd")
        self.btn_browsedict = QtWidgets.QPushButton(self.tab_dict_crack)
        self.btn_browsedict.setGeometry(QtCore.QRect(420, 0, 151, 31))
        self.btn_browsedict.setObjectName("btn_browsedict")
        self.cb_target = QtWidgets.QComboBox(self.tab_dict_crack)
        self.cb_target.setGeometry(QtCore.QRect(0, 30, 421, 31))
        self.cb_target.setObjectName("cb_target")
        self.cb_target.addItem("")
        self.btn_refresh = QtWidgets.QPushButton(self.tab_dict_crack)
        self.btn_refresh.setGeometry(QtCore.QRect(420, 30, 151, 31))
        self.btn_refresh.setObjectName("btn_refresh")
        self.cb_threads = QtWidgets.QComboBox(self.tab_dict_crack)
        self.cb_threads.setGeometry(QtCore.QRect(0, 60, 571, 31))
        self.cb_threads.setObjectName("cb_threads")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.cb_threads.addItem("")
        self.btn_start = QtWidgets.QCommandLinkButton(self.tab_dict_crack)
        self.btn_start.setGeometry(QtCore.QRect(0, 90, 571, 41))
        self.btn_start.setObjectName("btn_start")
        self.te_log = QtWidgets.QTextEdit(self.tab_dict_crack)
        self.te_log.setEnabled(True)
        self.te_log.setGeometry(QtCore.QRect(0, 130, 571, 161))
        self.te_log.setUndoRedoEnabled(False)
        self.te_log.setReadOnly(True)
        self.te_log.setObjectName("te_log")
        self.pb_progress = QtWidgets.QProgressBar(self.tab_dict_crack)
        self.pb_progress.setGeometry(QtCore.QRect(0, 290, 571, 23))
        self.pb_progress.setProperty("value", 0)
        self.pb_progress.setTextVisible(False)
        self.pb_progress.setObjectName("pb_progress")
        self.tabWidget_2.addTab(self.tab_dict_crack, "")
        self.tab_dict_gen = QtWidgets.QWidget()
        self.tab_dict_gen.setObjectName("tab_dict_gen")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_dict_gen)
        self.lineEdit.setGeometry(QtCore.QRect(0, 60, 571, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.check_num = QtWidgets.QCheckBox(self.tab_dict_gen)
        self.check_num.setGeometry(QtCore.QRect(0, 0, 281, 31))
        self.check_num.setObjectName("check_num")
        self.check_upper = QtWidgets.QCheckBox(self.tab_dict_gen)
        self.check_upper.setGeometry(QtCore.QRect(280, 0, 291, 31))
        self.check_upper.setObjectName("check_upper")
        self.check_lower = QtWidgets.QCheckBox(self.tab_dict_gen)
        self.check_lower.setGeometry(QtCore.QRect(0, 30, 281, 31))
        self.check_lower.setObjectName("check_lower")
        self.check_special = QtWidgets.QCheckBox(self.tab_dict_gen)
        self.check_special.setGeometry(QtCore.QRect(280, 30, 291, 31))
        self.check_special.setObjectName("check_special")
        self.btn_gen = QtWidgets.QCommandLinkButton(self.tab_dict_gen)
        self.btn_gen.setGeometry(QtCore.QRect(0, 90, 571, 41))
        self.btn_gen.setObjectName("btn_gen")
        self.gen_result = QtWidgets.QTextEdit(self.tab_dict_gen)
        self.gen_result.setGeometry(QtCore.QRect(0, 155, 571, 161))
        self.gen_result.setReadOnly(True)
        self.gen_result.setObjectName("gen_result")
        self.le_statu = QtWidgets.QLineEdit(self.tab_dict_gen)
        self.le_statu.setGeometry(QtCore.QRect(0, 120, 571, 31))
        self.le_statu.setReadOnly(True)
        self.le_statu.setObjectName("le_statu")
        self.tabWidget_2.addTab(self.tab_dict_gen, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dl_1 = QtWidgets.QCommandLinkButton(self.tab)
        self.dl_1.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.dl_1.setObjectName("dl_1")
        self.cl_2 = QtWidgets.QCommandLinkButton(self.tab)
        self.cl_2.setGeometry(QtCore.QRect(0, 40, 571, 41))
        self.cl_2.setObjectName("cl_2")
        self.cl_3 = QtWidgets.QCommandLinkButton(self.tab)
        self.cl_3.setGeometry(QtCore.QRect(0, 80, 571, 41))
        self.cl_3.setObjectName("cl_3")
        self.tabWidget_2.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_dict, "")
        self.tab_server = QtWidgets.QWidget()
        self.tab_server.setObjectName("tab_server")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_server)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 561, 301))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_getPwd = QtWidgets.QWidget()
        self.tab_getPwd.setObjectName("tab_getPwd")
        self.cb_getWIFI = QtWidgets.QComboBox(self.tab_getPwd)
        self.cb_getWIFI.setEnabled(False)
        self.cb_getWIFI.setGeometry(QtCore.QRect(0, 0, 451, 31))
        self.cb_getWIFI.setObjectName("cb_getWIFI")
        self.cb_getWIFI.addItem("")
        self.btn_refresh2 = QtWidgets.QPushButton(self.tab_getPwd)
        self.btn_refresh2.setEnabled(False)
        self.btn_refresh2.setGeometry(QtCore.QRect(450, 0, 111, 31))
        self.btn_refresh2.setObjectName("btn_refresh2")
        self.btn_get = QtWidgets.QCommandLinkButton(self.tab_getPwd)
        self.btn_get.setEnabled(False)
        self.btn_get.setGeometry(QtCore.QRect(0, 30, 551, 41))
        self.btn_get.setObjectName("btn_get")
        self.tabWidget_3.addTab(self.tab_getPwd, "")
        self.tab_upload = QtWidgets.QWidget()
        self.tab_upload.setObjectName("tab_upload")
        self.btn_upload = QtWidgets.QCommandLinkButton(self.tab_upload)
        self.btn_upload.setEnabled(False)
        self.btn_upload.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.btn_upload.setObjectName("btn_upload")
        self.tabWidget_3.addTab(self.tab_upload, "")
        self.le_svradd = QtWidgets.QLineEdit(self.tab_server)
        self.le_svradd.setGeometry(QtCore.QRect(0, 310, 471, 31))
        self.le_svradd.setObjectName("le_svradd")
        self.btn_connect = QtWidgets.QPushButton(self.tab_server)
        self.btn_connect.setGeometry(QtCore.QRect(470, 310, 91, 31))
        self.btn_connect.setObjectName("btn_connect")
        self.tabWidget.addTab(self.tab_server, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.le_dictadd.setPlaceholderText(_translate("MainWindow", "????????????"))
        self.btn_browsedict.setText(_translate("MainWindow", "??????"))
        self.cb_target.setItemText(0, _translate("MainWindow", "<????????????WIFI>"))
        self.btn_refresh.setText(_translate("MainWindow", "??????"))
        self.cb_threads.setItemText(0, _translate("MainWindow", "<??????????????????>"))
        self.cb_threads.setItemText(1, _translate("MainWindow", "?????????"))
        self.cb_threads.setItemText(2, _translate("MainWindow", "?????????"))
        self.cb_threads.setItemText(3, _translate("MainWindow", "?????????"))
        self.cb_threads.setItemText(4, _translate("MainWindow", "?????????"))
        self.cb_threads.setItemText(5, _translate("MainWindow", "????????????"))
        self.cb_threads.setItemText(6, _translate("MainWindow", "???????????????"))
        self.cb_threads.setItemText(7, _translate("MainWindow", "???????????????"))
        self.cb_threads.setItemText(8, _translate("MainWindow", "?????????????????????"))
        self.btn_start.setText(_translate("MainWindow", "????????????"))
        self.te_log.setPlaceholderText(_translate("MainWindow", "??????"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_dict_crack), _translate("MainWindow", "??????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "??????????????????"))
        self.check_num.setText(_translate("MainWindow", "??????(0-9)"))
        self.check_upper.setText(_translate("MainWindow", "????????????(A-Z)"))
        self.check_lower.setText(_translate("MainWindow", "????????????(a-z)"))
        self.check_special.setText(_translate("MainWindow", "????????????(!@#$%^&*()_+-=|;:\'\",<.>/?`~)"))
        self.btn_gen.setText(_translate("MainWindow", "??????"))
        self.gen_result.setPlaceholderText(_translate("MainWindow", "??????"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_dict_gen), _translate("MainWindow", "????????????"))
        self.dl_1.setText(_translate("MainWindow", "??????1"))
        self.cl_2.setText(_translate("MainWindow", "??????2"))
        self.cl_3.setText(_translate("MainWindow", "??????3"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dict), _translate("MainWindow", "????????????"))
        self.cb_getWIFI.setItemText(0, _translate("MainWindow", "<????????????WIFI>"))
        self.btn_refresh2.setText(_translate("MainWindow", "??????"))
        self.btn_get.setText(_translate("MainWindow", "??????"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_getPwd), _translate("MainWindow", "??????????????????"))
        self.btn_upload.setText(_translate("MainWindow", "??????"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_upload), _translate("MainWindow", "??????????????????"))
        self.le_svradd.setPlaceholderText(_translate("MainWindow", "?????????????????????"))
        self.btn_connect.setText(_translate("MainWindow", "??????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_server), _translate("MainWindow", "???????????????"))
