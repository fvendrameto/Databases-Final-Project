# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'casadefesta.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 340)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(460, 16777215))
        self.cidade_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.cidade_lineEdit.setGeometry(QtCore.QRect(30, 190, 121, 28))
        self.cidade_lineEdit.setObjectName("cidade_lineEdit")
        self.rua_label = QtWidgets.QLabel(Dialog)
        self.rua_label.setGeometry(QtCore.QRect(30, 110, 58, 16))
        self.rua_label.setObjectName("rua_label")
        self.rua_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.rua_lineEdit.setGeometry(QtCore.QRect(30, 130, 121, 28))
        self.rua_lineEdit.setObjectName("rua_lineEdit")
        self.estado_label = QtWidgets.QLabel(Dialog)
        self.estado_label.setGeometry(QtCore.QRect(160, 170, 41, 16))
        self.estado_label.setObjectName("estado_label")
        self.n_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.n_lineEdit.setGeometry(QtCore.QRect(160, 130, 41, 28))
        self.n_lineEdit.setObjectName("n_lineEdit")
        self.cidade_label = QtWidgets.QLabel(Dialog)
        self.cidade_label.setGeometry(QtCore.QRect(30, 170, 58, 16))
        self.cidade_label.setObjectName("cidade_label")
        self.endereco_label = QtWidgets.QLabel(Dialog)
        self.endereco_label.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.endereco_label.setObjectName("endereco_label")
        self.n_label = QtWidgets.QLabel(Dialog)
        self.n_label.setGeometry(QtCore.QRect(160, 110, 21, 16))
        self.n_label.setObjectName("n_label")
        self.estado_comboBox = QtWidgets.QComboBox(Dialog)
        self.estado_comboBox.setGeometry(QtCore.QRect(160, 190, 41, 28))
        self.estado_comboBox.setObjectName("estado_comboBox")
        self.nome_label = QtWidgets.QLabel(Dialog)
        self.nome_label.setGeometry(QtCore.QRect(20, 20, 58, 16))
        self.nome_label.setObjectName("nome_label")
        self.nome_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.nome_lineEdit.setGeometry(QtCore.QRect(20, 40, 201, 28))
        self.nome_lineEdit.setMaxLength(75)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(25, 290, 190, 34))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.cep_label = QtWidgets.QLabel(Dialog)
        self.cep_label.setGeometry(QtCore.QRect(30, 230, 58, 16))
        self.cep_label.setObjectName("cep_label")
        self.cep_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.cep_lineEdit.setGeometry(QtCore.QRect(30, 250, 181, 28))
        self.cep_lineEdit.setMaxLength(9)
        self.cep_lineEdit.setObjectName("cep_lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rua_label.setText(_translate("Dialog", "Rua"))
        self.estado_label.setText(_translate("Dialog", "Estado"))
        self.cidade_label.setText(_translate("Dialog", "Cidade"))
        self.endereco_label.setText(_translate("Dialog", "Endereço"))
        self.n_label.setText(_translate("Dialog", "Nº"))
        self.nome_label.setText(_translate("Dialog", "Nome"))
        self.cep_label.setText(_translate("Dialog", "CEP"))
        self.cep_lineEdit.setInputMask(_translate("Dialog", "99999-999"))

