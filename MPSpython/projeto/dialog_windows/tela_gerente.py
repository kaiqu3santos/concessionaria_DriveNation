# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_gerente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(906, 620)
        Dialog.setMaximumSize(QtCore.QSize(906, 620))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(78, 110, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(370, 0, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.right_menu = QtWidgets.QFrame(self.frame)
        self.right_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_menu.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.right_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_menu.setObjectName("right_menu")
        self.label_5 = QtWidgets.QLabel(self.right_menu)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 411, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.right_menu)
        self.label_6.setGeometry(QtCore.QRect(50, 310, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.right_menu)
        self.left_menu = QtWidgets.QFrame(self.frame)
        self.left_menu.setMaximumSize(QtCore.QSize(400, 16777215))
        self.left_menu.setStyleSheet("background-color: rgb(116, 169, 255)")
        self.left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu.setObjectName("left_menu")
        self.pushButton_9 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 320, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 220, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_11.setGeometry(QtCore.QRect(80, 270, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 170, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 520, 93, 28))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 74, 116);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 120, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_15.setGeometry(QtCore.QRect(80, 70, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.left_menu)
        self.pushButton_16.setGeometry(QtCore.QRect(80, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(42, 99, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.left_menu)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "ÁREA DO GERENTE"))
        self.label_5.setText(_translate("Dialog", "Concessionária \n"
"DriveNation"))
        self.label_6.setText(_translate("Dialog", "Você mais veloz"))
        self.pushButton_9.setText(_translate("Dialog", "VISUALIZAR FATURAMENTO"))
        self.pushButton_10.setText(_translate("Dialog", "GERENCIAR FATURAMENTO"))
        self.pushButton_11.setText(_translate("Dialog", "VISUALIZAR FUNCIONÁRIOS"))
        self.pushButton_12.setText(_translate("Dialog", "CADASTRAR VEÍCULO"))
        self.pushButton_13.setText(_translate("Dialog", "LOGOFF"))
        self.pushButton_14.setText(_translate("Dialog", "CADASTRAR FUNCIONÁRIO"))
        self.pushButton_15.setText(_translate("Dialog", "VISUALIZAR VEÍCULO"))
        self.pushButton_16.setText(_translate("Dialog", "FUNCIONÁRIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
