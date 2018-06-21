# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Funcionario(object):
    def setupUi(self, Funcionario):
        Funcionario.setObjectName("Funcionario")
        Funcionario.resize(460, 270)
        Funcionario.setMinimumSize(QtCore.QSize(460, 270))
        Funcionario.setMaximumSize(QtCore.QSize(460, 270))
        Funcionario.setBaseSize(QtCore.QSize(240, 440))
        self.cpf_label = QtWidgets.QLabel(Funcionario)
        self.cpf_label.setGeometry(QtCore.QRect(20, 20, 58, 16))
        self.cpf_label.setObjectName("cpf_label")
        self.cpf_lineEdit = QtWidgets.QLineEdit(Funcionario)
        self.cpf_lineEdit.setGeometry(QtCore.QRect(20, 40, 201, 28))
        self.cpf_lineEdit.setMaxLength(14)
        self.cpf_lineEdit.setPlaceholderText("")
        self.cpf_lineEdit.setObjectName("cpf_lineEdit")
        self.nome_lineEdit = QtWidgets.QLineEdit(Funcionario)
        self.nome_lineEdit.setGeometry(QtCore.QRect(20, 100, 201, 28))
        self.nome_lineEdit.setMaxLength(75)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.nome_label = QtWidgets.QLabel(Funcionario)
        self.nome_label.setGeometry(QtCore.QRect(20, 80, 58, 16))
        self.nome_label.setObjectName("nome_label")
        self.telFixo_lineEdit = QtWidgets.QLineEdit(Funcionario)
        self.telFixo_lineEdit.setGeometry(QtCore.QRect(240, 40, 201, 28))
        self.telFixo_lineEdit.setMaxLength(13)
        self.telFixo_lineEdit.setPlaceholderText("")
        self.telFixo_lineEdit.setObjectName("telFixo_lineEdit")
        self.telFixo_label = QtWidgets.QLabel(Funcionario)
        self.telFixo_label.setGeometry(QtCore.QRect(240, 20, 81, 16))
        self.telFixo_label.setObjectName("telFixo_label")
        self.telMovel_label = QtWidgets.QLabel(Funcionario)
        self.telMovel_label.setGeometry(QtCore.QRect(240, 80, 101, 16))
        self.telMovel_label.setObjectName("telMovel_label")
        self.telMovel_lineEdit = QtWidgets.QLineEdit(Funcionario)
        self.telMovel_lineEdit.setGeometry(QtCore.QRect(240, 100, 201, 28))
        self.telMovel_lineEdit.setMaxLength(14)
        self.telMovel_lineEdit.setPlaceholderText("")
        self.telMovel_lineEdit.setObjectName("telMovel_lineEdit")
        self.comissao_label = QtWidgets.QLabel(Funcionario)
        self.comissao_label.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.comissao_label.setObjectName("comissao_label")
        self.comissao_spinBox = QtWidgets.QDoubleSpinBox(Funcionario)
        self.comissao_spinBox.setGeometry(QtCore.QRect(20, 160, 201, 28))
        self.comissao_spinBox.setObjectName("comissao_spinBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(Funcionario)
        self.buttonBox.setGeometry(QtCore.QRect(135, 220, 190, 34))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.cargo_label = QtWidgets.QLabel(Funcionario)
        self.cargo_label.setGeometry(QtCore.QRect(240, 140, 58, 16))
        self.cargo_label.setObjectName("cargo_label")
        self.cargo_comboBox = QtWidgets.QComboBox(Funcionario)
        self.cargo_comboBox.setGeometry(QtCore.QRect(240, 160, 201, 28))
        self.cargo_comboBox.setObjectName("cargo_comboBox")

        self.retranslateUi(Funcionario)
        QtCore.QMetaObject.connectSlotsByName(Funcionario)

    def retranslateUi(self, Funcionario):
        _translate = QtCore.QCoreApplication.translate
        Funcionario.setWindowTitle(_translate("Funcionario", "Dialog"))
        self.cpf_label.setText(_translate("Funcionario", "CPF"))
        self.cpf_lineEdit.setInputMask(_translate("Funcionario", "999.999.999-99"))
        self.nome_label.setText(_translate("Funcionario", "Nome"))
        self.telFixo_lineEdit.setInputMask(_translate("Funcionario", "(99)9999-9999"))
        self.telFixo_label.setText(_translate("Funcionario", "Telefone Fixo"))
        self.telMovel_label.setText(_translate("Funcionario", "Telefone Móvel"))
        self.telMovel_lineEdit.setInputMask(_translate("Funcionario", "(99)99999-9999"))
        self.comissao_label.setText(_translate("Funcionario", "Comissão"))
        self.cargo_label.setText(_translate("Funcionario", "Cargo"))

