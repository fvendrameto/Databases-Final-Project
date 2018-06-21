# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fornecedor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 270)
        Dialog.setMinimumSize(QtCore.QSize(460, 270))
        Dialog.setMaximumSize(QtCore.QSize(460, 270))
        self.cnpj_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.cnpj_lineEdit.setGeometry(QtCore.QRect(20, 40, 201, 28))
        self.cnpj_lineEdit.setMaximumSize(QtCore.QSize(240, 440))
        self.cnpj_lineEdit.setObjectName("cnpj_lineEdit")
        self.cnpj_label = QtWidgets.QLabel(Dialog)
        self.cnpj_label.setGeometry(QtCore.QRect(20, 20, 58, 16))
        self.cnpj_label.setObjectName("cnpj_label")
        self.nome_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.nome_lineEdit.setGeometry(QtCore.QRect(20, 100, 201, 28))
        self.nome_lineEdit.setMaximumSize(QtCore.QSize(240, 440))
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.nome_label = QtWidgets.QLabel(Dialog)
        self.nome_label.setGeometry(QtCore.QRect(20, 80, 58, 16))
        self.nome_label.setObjectName("nome_label")
        self.tel_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.tel_lineEdit.setGeometry(QtCore.QRect(20, 160, 201, 28))
        self.tel_lineEdit.setMaximumSize(QtCore.QSize(240, 440))
        self.tel_lineEdit.setObjectName("tel_lineEdit")
        self.tel_label = QtWidgets.QLabel(Dialog)
        self.tel_label.setGeometry(QtCore.QRect(20, 140, 58, 16))
        self.tel_label.setObjectName("tel_label")
        self.dadosBancarios_label = QtWidgets.QLabel(Dialog)
        self.dadosBancarios_label.setGeometry(QtCore.QRect(240, 20, 101, 16))
        self.dadosBancarios_label.setObjectName("dadosBancarios_label")
        self.banco_comboBox = QtWidgets.QComboBox(Dialog)
        self.banco_comboBox.setGeometry(QtCore.QRect(250, 60, 181, 28))
        self.banco_comboBox.setObjectName("banco_comboBox")
        self.banco_label = QtWidgets.QLabel(Dialog)
        self.banco_label.setGeometry(QtCore.QRect(250, 50, 101, 16))
        self.banco_label.setObjectName("banco_label")
        self.agencia_label = QtWidgets.QLabel(Dialog)
        self.agencia_label.setGeometry(QtCore.QRect(250, 100, 51, 16))
        self.agencia_label.setObjectName("agencia_label")
        self.conta_label = QtWidgets.QLabel(Dialog)
        self.conta_label.setGeometry(QtCore.QRect(310, 100, 51, 16))
        self.conta_label.setObjectName("conta_label")
        self.agencia_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.agencia_lineEdit.setGeometry(QtCore.QRect(250, 120, 51, 28))
        self.agencia_lineEdit.setObjectName("agencia_lineEdit")
        self.conta_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.conta_lineEdit.setGeometry(QtCore.QRect(310, 120, 121, 28))
        self.conta_lineEdit.setObjectName("conta_lineEdit")
        self.corrente_radioButton = QtWidgets.QRadioButton(Dialog)
        self.corrente_radioButton.setGeometry(QtCore.QRect(250, 160, 81, 28))
        self.corrente_radioButton.setObjectName("corrente_radioButton")
        self.poupanca_radioButton = QtWidgets.QRadioButton(Dialog)
        self.poupanca_radioButton.setGeometry(QtCore.QRect(340, 160, 81, 28))
        self.poupanca_radioButton.setObjectName("poupanca_radioButton")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(135, 220, 190, 34))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cnpj_lineEdit.setInputMask(_translate("Dialog", "99.999.999/9999-99"))
        self.cnpj_label.setText(_translate("Dialog", "CNPJ"))
        self.nome_label.setText(_translate("Dialog", "Nome"))
        self.tel_lineEdit.setInputMask(_translate("Dialog", "(99)99999-9999"))
        self.tel_label.setText(_translate("Dialog", "Telefone"))
        self.dadosBancarios_label.setText(_translate("Dialog", "Dados Bancários"))
        self.banco_label.setText(_translate("Dialog", "Banco"))
        self.agencia_label.setText(_translate("Dialog", "Agência"))
        self.conta_label.setText(_translate("Dialog", "Conta"))
        self.agencia_lineEdit.setInputMask(_translate("Dialog", "9999"))
        self.conta_lineEdit.setInputMask(_translate("Dialog", "9999999999"))
        self.corrente_radioButton.setText(_translate("Dialog", "Corrente"))
        self.poupanca_radioButton.setText(_translate("Dialog", "Poupança"))

