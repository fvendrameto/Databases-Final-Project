# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/cliente.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 470)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_8 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.frame_3)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.telFixo_label = QtWidgets.QLabel(self.widget_2)
        self.telFixo_label.setObjectName("telFixo_label")
        self.gridLayout_5.addWidget(self.telFixo_label, 0, 0, 1, 1)
        self.telMovel_label = QtWidgets.QLabel(self.widget_2)
        self.telMovel_label.setObjectName("telMovel_label")
        self.gridLayout_5.addWidget(self.telMovel_label, 0, 1, 1, 1)
        self.telFixo_lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.telFixo_lineEdit.setMaxLength(13)
        self.telFixo_lineEdit.setPlaceholderText("")
        self.telFixo_lineEdit.setObjectName("telFixo_lineEdit")
        self.gridLayout_5.addWidget(self.telFixo_lineEdit, 1, 0, 1, 1)
        self.telMovel_lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.telMovel_lineEdit.setMaxLength(14)
        self.telMovel_lineEdit.setPlaceholderText("")
        self.telMovel_lineEdit.setObjectName("telMovel_lineEdit")
        self.gridLayout_5.addWidget(self.telMovel_lineEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 2, 1, 1)
        self.gridLayout_7.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.frame_3)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cpf_label = QtWidgets.QLabel(self.widget_3)
        self.cpf_label.setObjectName("cpf_label")
        self.gridLayout_4.addWidget(self.cpf_label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.cpf_lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.cpf_lineEdit.setMaxLength(14)
        self.cpf_lineEdit.setPlaceholderText("")
        self.cpf_lineEdit.setObjectName("cpf_lineEdit")
        self.gridLayout_4.addWidget(self.cpf_lineEdit, 1, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_7.addWidget(self.widget_3, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nome_label = QtWidgets.QLabel(self.widget_4)
        self.nome_label.setObjectName("nome_label")
        self.gridLayout_6.addWidget(self.nome_label, 0, 0, 1, 1)
        self.nome_lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.nome_lineEdit.setMaxLength(75)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.gridLayout_6.addWidget(self.nome_lineEdit, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_4, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_3, 1, 0, 1, 2)
        self.dadosBancarios_label = QtWidgets.QLabel(Dialog)
        self.dadosBancarios_label.setObjectName("dadosBancarios_label")
        self.gridLayout_8.addWidget(self.dadosBancarios_label, 2, 0, 1, 1)
        self.endereco_label = QtWidgets.QLabel(Dialog)
        self.endereco_label.setObjectName("endereco_label")
        self.gridLayout_8.addWidget(self.endereco_label, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.banco_label = QtWidgets.QLabel(self.widget_5)
        self.banco_label.setObjectName("banco_label")
        self.gridLayout_2.addWidget(self.banco_label, 0, 0, 1, 1)
        self.banco_comboBox = QtWidgets.QComboBox(self.widget_5)
        self.banco_comboBox.setObjectName("banco_comboBox")
        self.gridLayout_2.addWidget(self.banco_comboBox, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.widget_5, 0, 0, 1, 3)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.agencia_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.agencia_lineEdit.setObjectName("agencia_lineEdit")
        self.gridLayout.addWidget(self.agencia_lineEdit, 1, 0, 1, 1)
        self.conta_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.conta_lineEdit.setObjectName("conta_lineEdit")
        self.gridLayout.addWidget(self.conta_lineEdit, 1, 1, 1, 1)
        self.agencia_label = QtWidgets.QLabel(self.widget)
        self.agencia_label.setObjectName("agencia_label")
        self.gridLayout.addWidget(self.agencia_label, 0, 0, 1, 1)
        self.conta_label = QtWidgets.QLabel(self.widget)
        self.conta_label.setObjectName("conta_label")
        self.gridLayout.addWidget(self.conta_label, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout_9.addWidget(self.widget, 1, 0, 1, 3)
        self.corrente_radioButton = QtWidgets.QRadioButton(self.frame)
        self.corrente_radioButton.setObjectName("corrente_radioButton")
        self.gridLayout_9.addWidget(self.corrente_radioButton, 2, 0, 1, 1)
        self.poupanca_radioButton = QtWidgets.QRadioButton(self.frame)
        self.poupanca_radioButton.setObjectName("poupanca_radioButton")
        self.gridLayout_9.addWidget(self.poupanca_radioButton, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 2, 2, 1, 1)
        self.gridLayout_8.addWidget(self.frame, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rua_label = QtWidgets.QLabel(self.frame_2)
        self.rua_label.setObjectName("rua_label")
        self.gridLayout_3.addWidget(self.rua_label, 0, 0, 1, 1)
        self.n_label = QtWidgets.QLabel(self.frame_2)
        self.n_label.setObjectName("n_label")
        self.gridLayout_3.addWidget(self.n_label, 0, 1, 1, 1)
        self.rua_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.rua_lineEdit.setMaxLength(50)
        self.rua_lineEdit.setObjectName("rua_lineEdit")
        self.gridLayout_3.addWidget(self.rua_lineEdit, 1, 0, 1, 1)
        self.n_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.n_lineEdit.setMaxLength(5)
        self.n_lineEdit.setObjectName("n_lineEdit")
        self.gridLayout_3.addWidget(self.n_lineEdit, 1, 1, 1, 1)
        self.cidade_label = QtWidgets.QLabel(self.frame_2)
        self.cidade_label.setObjectName("cidade_label")
        self.gridLayout_3.addWidget(self.cidade_label, 2, 0, 1, 1)
        self.estado_label = QtWidgets.QLabel(self.frame_2)
        self.estado_label.setObjectName("estado_label")
        self.gridLayout_3.addWidget(self.estado_label, 2, 1, 1, 1)
        self.cidade_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.cidade_lineEdit.setMaxLength(20)
        self.cidade_lineEdit.setObjectName("cidade_lineEdit")
        self.gridLayout_3.addWidget(self.cidade_lineEdit, 3, 0, 1, 1)
        self.estado_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.estado_comboBox.setObjectName("estado_comboBox")
        self.gridLayout_3.addWidget(self.estado_comboBox, 3, 1, 1, 1)
        self.cep_label = QtWidgets.QLabel(self.frame_2)
        self.cep_label.setObjectName("cep_label")
        self.gridLayout_3.addWidget(self.cep_label, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 1, 2, 1)
        self.cep_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.cep_lineEdit.setMaxLength(9)
        self.cep_lineEdit.setObjectName("cep_lineEdit")
        self.gridLayout_3.addWidget(self.cep_lineEdit, 5, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_8.addWidget(self.frame_2, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(283, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_8.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Dados Pessoais"))
        self.telFixo_label.setText(_translate("Dialog", "Telefone Fixo"))
        self.telMovel_label.setText(_translate("Dialog", "Telefone Móvel"))
        self.telFixo_lineEdit.setInputMask(_translate("Dialog", "(99)9999-9999"))
        self.telMovel_lineEdit.setInputMask(_translate("Dialog", "(99)99999-9999"))
        self.cpf_label.setText(_translate("Dialog", "CPF"))
        self.cpf_lineEdit.setInputMask(_translate("Dialog", "999.999.999-99"))
        self.nome_label.setText(_translate("Dialog", "Nome"))
        self.dadosBancarios_label.setText(_translate("Dialog", "Dados Bancários"))
        self.endereco_label.setText(_translate("Dialog", "Endereço"))
        self.banco_label.setText(_translate("Dialog", "Banco"))
        self.agencia_lineEdit.setInputMask(_translate("Dialog", "9999"))
        self.conta_lineEdit.setInputMask(_translate("Dialog", "9999999999"))
        self.agencia_label.setText(_translate("Dialog", "Agência"))
        self.conta_label.setText(_translate("Dialog", "Conta"))
        self.corrente_radioButton.setText(_translate("Dialog", "Corrente"))
        self.poupanca_radioButton.setText(_translate("Dialog", "Poupança"))
        self.rua_label.setText(_translate("Dialog", "Rua"))
        self.n_label.setText(_translate("Dialog", "Nº"))
        self.n_lineEdit.setInputMask(_translate("Dialog", "99999"))
        self.cidade_label.setText(_translate("Dialog", "Cidade"))
        self.estado_label.setText(_translate("Dialog", "Estado"))
        self.cep_label.setText(_translate("Dialog", "CEP"))
        self.cep_lineEdit.setInputMask(_translate("Dialog", "99999-999"))

