# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitProjects\MisakMikot\practice\SimpleExplorer\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(960, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Delete = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete.sizePolicy().hasHeightForWidth())
        self.Delete.setSizePolicy(sizePolicy)
        self.Delete.setMinimumSize(QtCore.QSize(0, 60))
        self.Delete.setObjectName("Delete")
        self.horizontalLayout_3.addWidget(self.Delete)
        self.Copy = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Copy.sizePolicy().hasHeightForWidth())
        self.Copy.setSizePolicy(sizePolicy)
        self.Copy.setMinimumSize(QtCore.QSize(0, 60))
        self.Copy.setObjectName("Copy")
        self.horizontalLayout_3.addWidget(self.Copy)
        self.Paste = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Paste.sizePolicy().hasHeightForWidth())
        self.Paste.setSizePolicy(sizePolicy)
        self.Paste.setMinimumSize(QtCore.QSize(0, 60))
        self.Paste.setObjectName("Paste")
        self.horizontalLayout_3.addWidget(self.Paste)
        self.Rename = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rename.sizePolicy().hasHeightForWidth())
        self.Rename.setSizePolicy(sizePolicy)
        self.Rename.setMinimumSize(QtCore.QSize(0, 60))
        self.Rename.setObjectName("Rename")
        self.horizontalLayout_3.addWidget(self.Rename)
        self.copyPath = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyPath.sizePolicy().hasHeightForWidth())
        self.copyPath.setSizePolicy(sizePolicy)
        self.copyPath.setMinimumSize(QtCore.QSize(0, 60))
        self.copyPath.setObjectName("copyPath")
        self.horizontalLayout_3.addWidget(self.copyPath)
        self.Notepad = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Notepad.sizePolicy().hasHeightForWidth())
        self.Notepad.setSizePolicy(sizePolicy)
        self.Notepad.setMinimumSize(QtCore.QSize(0, 60))
        self.Notepad.setObjectName("Notepad")
        self.horizontalLayout_3.addWidget(self.Notepad)
        self.calcHash = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcHash.sizePolicy().hasHeightForWidth())
        self.calcHash.setSizePolicy(sizePolicy)
        self.calcHash.setMinimumSize(QtCore.QSize(0, 60))
        self.calcHash.setObjectName("calcHash")
        self.horizontalLayout_3.addWidget(self.calcHash)
        self.openInExplorer = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openInExplorer.sizePolicy().hasHeightForWidth())
        self.openInExplorer.setSizePolicy(sizePolicy)
        self.openInExplorer.setMinimumSize(QtCore.QSize(0, 60))
        self.openInExplorer.setObjectName("openInExplorer")
        self.horizontalLayout_3.addWidget(self.openInExplorer)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeView = QtWidgets.QTreeView(Widget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_2.addWidget(self.treeView)
        self.horizontalLayout_2.setStretch(0, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar = QtWidgets.QProgressBar(Widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.label = QtWidgets.QLabel(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_5.setStretch(0, 8)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.progressBar_2 = QtWidgets.QProgressBar(Widget)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_6.addWidget(self.progressBar_2)
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_6.setStretch(0, 8)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.Delete.setText(_translate("Widget", "??????"))
        self.Copy.setText(_translate("Widget", "??????"))
        self.Paste.setText(_translate("Widget", "??????"))
        self.Rename.setText(_translate("Widget", "?????????"))
        self.copyPath.setText(_translate("Widget", "????????????"))
        self.Notepad.setText(_translate("Widget", "?????????"))
        self.calcHash.setText(_translate("Widget", "??????Hash"))
        self.openInExplorer.setText(_translate("Widget", "???????????????"))
        self.pushButton.setText(_translate("Widget", "??????"))
        self.label.setText(_translate("Widget", "0 MB / 0 MB"))
        self.label_2.setText(_translate("Widget", "0 / 0"))
