# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controles import C_EfetuarLogon
import F_tela_gerente
import F_tela_funcionario
import F_veiculos

class Ui_MainWindow(object):

    #--------------------------------------------FRONTEIRA--------------------------------------------
    def f_efetuar_login(self, MainWindow):
        gmail = self.lineEdit.text()
        senha = self.lineEdit_2.text()
        if gmail != "" and senha != "":
            C_EfetuarLogon(self, gmail, senha)

    def tela_gerente (self, gmail):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = F_tela_gerente.Ui_MainWindow()
        gmail = self.lineEdit.text()
        self.ui.setupUi(self.window2, gmail)
        self.window2.show()
    
    def tela_funcionario(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = F_tela_funcionario.Ui_MainWindow()
        gmail = self.lineEdit.text()
        self.ui.setupUi(self.window2, gmail)
        self.window2.show()

    #-------------------------------------------------------------------------------------------------

    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(78, 110, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.top_menu = QtWidgets.QFrame(self.centralwidget)
        self.top_menu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu.setObjectName("top_menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.right_menu = QtWidgets.QFrame(self.top_menu)
        self.right_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_menu.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.right_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_menu.setObjectName("right_menu")
        self.label_2 = QtWidgets.QLabel(self.right_menu)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 411, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.right_menu)
        self.label_3.setGeometry(QtCore.QRect(50, 310, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.right_menu)
        self.left_menu = QtWidgets.QFrame(self.top_menu)
        self.left_menu.setMaximumSize(QtCore.QSize(400, 16777215))
        self.left_menu.setStyleSheet("background-color: rgb(116, 169, 255)")
        self.left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu.setObjectName("left_menu")
        self.pushButton = QtWidgets.QPushButton(self.left_menu)
        self.pushButton.setGeometry(QtCore.QRect(170, 350, 93, 28))
        self.pushButton.setObjectName("pushButton")
#       self.pushButton.clicked.connect(self.tela_funcionario)
        self.label = QtWidgets.QLabel(self.left_menu)
        self.label.setGeometry(QtCore.QRect(170, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.left_menu)
        self.lineEdit.setGeometry(QtCore.QRect(120, 250, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.left_menu)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 290, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.left_menu)
        self.verticalLayout.addWidget(self.top_menu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Concessionária \n"
"DriveNation"))
        self.label_3.setText(_translate("MainWindow", "Você mais veloz"))
        self.pushButton.setText(_translate("MainWindow", "ENTRAR"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit.setText(_translate("MainWindow", "admin"))
        self.lineEdit_2.setText(_translate("MainWindow", "1234"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda:ui.f_efetuar_login(MainWindow))                                                                    
    MainWindow.show()
    sys.exit(app.exec_())