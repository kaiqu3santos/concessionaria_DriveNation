# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cad_veiculo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Controles

class Ui_MainWindow(object):

    #--------------------------------------------FRONTEIRA--------------------------------------------
 
    def f_cad_veiculo(self):
        placa = self.lineEdit_3.text()
        marca = self.lineEdit_8.text()
        modelo = self.lineEdit_4.text()
        cor = self.lineEdit_5.text()
        combustivel = self.lineEdit.text()
        valor = self.lineEdit_2.text()
        especificacoes = self.textEdit.toPlainText()
        if placa != "PLACA" and placa != "" and marca != "" and modelo != "" and cor != "" and combustivel != "" and valor != "" and especificacoes != "":
            Controles.C_CadastrarVeiculo(placa, marca, modelo, cor, combustivel, valor, especificacoes)

            self.MainWindow.close()

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
        self.frame_2.setStyleSheet("background-color: rgb(78, 110, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(350, 10, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(80, 300, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(80, 180, 411, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setStyleSheet("background-color: rgb(116, 169, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 120, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(70, 160, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_17.setGeometry(QtCore.QRect(300, 530, 93, 28))
        self.pushButton_17.setStyleSheet("background-color: rgb(255, 74, 116);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 80, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 240, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setGeometry(QtCore.QRect(70, 280, 281, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_18.setGeometry(QtCore.QRect(160, 480, 93, 28))
        self.pushButton_18.setStyleSheet("background-color: rgb(78, 110, 255);\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "CADASTRAR VEÍCULO"))
        self.label_9.setText(_translate("MainWindow", "Você mais veloz"))
        self.label_8.setText(_translate("MainWindow", "Concessionária \n"
"DriveNation"))
        self.lineEdit_5.setText(_translate("MainWindow", "COR"))
        self.lineEdit.setText(_translate("MainWindow", "COMBUSTÍVEL"))
        self.pushButton_17.setText(_translate("MainWindow", "VOLTAR"))
        self.pushButton_17.clicked.connect(lambda:self.MainWindow.close())
        self.lineEdit_4.setText(_translate("MainWindow", "MODELO"))
        self.lineEdit_2.setText(_translate("MainWindow", "VALOR"))
        self.lineEdit_3.setText(_translate("MainWindow", "PLACA"))
        self.lineEdit_8.setText(_translate("MainWindow", "MARCA"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ESPECIFICAÇÕES</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_18.setText(_translate("MainWindow", "CADASTRAR"))
        self.pushButton_18.clicked.connect(lambda:self.f_cad_veiculo())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
