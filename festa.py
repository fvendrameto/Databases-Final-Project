# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'festa.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_Festa(object):
    def setupUi(self, Add_Festa):
        Add_Festa.setObjectName("Add_Festa")
        Add_Festa.resize(845, 559)
        self.cliente_label = QtWidgets.QLabel(Add_Festa)
        self.cliente_label.setGeometry(QtCore.QRect(20, 20, 58, 16))
        self.cliente_label.setObjectName("cliente_label")
        self.cliente_comboBox = QtWidgets.QComboBox(Add_Festa)
        self.cliente_comboBox.setGeometry(QtCore.QRect(20, 40, 281, 28))
        self.cliente_comboBox.setObjectName("cliente_comboBox")
        self.cliente_pushButton = QtWidgets.QPushButton(Add_Festa)
        self.cliente_pushButton.setGeometry(QtCore.QRect(310, 40, 92, 34))
        self.cliente_pushButton.setObjectName("cliente_pushButton")
        self.data_timeEdit = QtWidgets.QDateTimeEdit(Add_Festa)
        self.data_timeEdit.setGeometry(QtCore.QRect(20, 100, 194, 28))
        self.data_timeEdit.setObjectName("data_timeEdit")
        self.data_label = QtWidgets.QLabel(Add_Festa)
        self.data_label.setGeometry(QtCore.QRect(20, 80, 58, 16))
        self.data_label.setObjectName("data_label")
        self.convidados_spinBox = QtWidgets.QSpinBox(Add_Festa)
        self.convidados_spinBox.setGeometry(QtCore.QRect(20, 160, 104, 28))
        self.convidados_spinBox.setMaximum(99999)
        self.convidados_spinBox.setObjectName("convidados_spinBox")
        self.convidados_label = QtWidgets.QLabel(Add_Festa)
        self.convidados_label.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.convidados_label.setObjectName("convidados_label")
        self.preco_spinBox = QtWidgets.QDoubleSpinBox(Add_Festa)
        self.preco_spinBox.setGeometry(QtCore.QRect(130, 160, 132, 28))
        self.preco_spinBox.setMaximum(999999.99)
        self.preco_spinBox.setObjectName("preco_spinBox")
        self.preco_label = QtWidgets.QLabel(Add_Festa)
        self.preco_label.setGeometry(QtCore.QRect(130, 140, 71, 16))
        self.preco_label.setObjectName("preco_label")
        self.casaDeFesta_label = QtWidgets.QLabel(Add_Festa)
        self.casaDeFesta_label.setGeometry(QtCore.QRect(20, 200, 81, 16))
        self.casaDeFesta_label.setObjectName("casaDeFesta_label")
        self.casaDeFesta_pushButton = QtWidgets.QPushButton(Add_Festa)
        self.casaDeFesta_pushButton.setGeometry(QtCore.QRect(310, 220, 92, 34))
        self.casaDeFesta_pushButton.setObjectName("casaDeFesta_pushButton")
        self.casaDeFesta_comboBox = QtWidgets.QComboBox(Add_Festa)
        self.casaDeFesta_comboBox.setGeometry(QtCore.QRect(20, 220, 281, 28))
        self.casaDeFesta_comboBox.setObjectName("casaDeFesta_comboBox")
        self.gerente_pushButton = QtWidgets.QPushButton(Add_Festa)
        self.gerente_pushButton.setGeometry(QtCore.QRect(310, 280, 92, 34))
        self.gerente_pushButton.setObjectName("gerente_pushButton")
        self.gerente_label = QtWidgets.QLabel(Add_Festa)
        self.gerente_label.setGeometry(QtCore.QRect(20, 260, 81, 16))
        self.gerente_label.setObjectName("gerente_label")
        self.gerente_comboBox = QtWidgets.QComboBox(Add_Festa)
        self.gerente_comboBox.setGeometry(QtCore.QRect(20, 280, 281, 28))
        self.gerente_comboBox.setObjectName("gerente_comboBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(Add_Festa)
        self.buttonBox.setGeometry(QtCore.QRect(640, 510, 190, 34))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.bebida_label = QtWidgets.QLabel(Add_Festa)
        self.bebida_label.setGeometry(QtCore.QRect(440, 20, 58, 16))
        self.bebida_label.setObjectName("bebida_label")
        self.bebida_comboBox = QtWidgets.QComboBox(Add_Festa)
        self.bebida_comboBox.setGeometry(QtCore.QRect(440, 40, 231, 28))
        self.bebida_comboBox.setObjectName("bebida_comboBox")
        self.quantidade_pushButton = QtWidgets.QPushButton(Add_Festa)
        self.quantidade_pushButton.setGeometry(QtCore.QRect(800, 40, 31, 34))
        self.quantidade_pushButton.setObjectName("quantidade_pushButton")
        self.quantidade_label = QtWidgets.QLabel(Add_Festa)
        self.quantidade_label.setGeometry(QtCore.QRect(690, 20, 71, 16))
        self.quantidade_label.setObjectName("quantidade_label")
        self.quantidade_spinBox = QtWidgets.QSpinBox(Add_Festa)
        self.quantidade_spinBox.setGeometry(QtCore.QRect(690, 40, 104, 28))
        self.quantidade_spinBox.setMaximum(99999)
        self.quantidade_spinBox.setObjectName("quantidade_spinBox")
        self.barracas_spinBox = QtWidgets.QSpinBox(Add_Festa)
        self.barracas_spinBox.setGeometry(QtCore.QRect(20, 460, 141, 28))
        self.barracas_spinBox.setMaximum(99999)
        self.barracas_spinBox.setObjectName("barracas_spinBox")
        self.barracas_label = QtWidgets.QLabel(Add_Festa)
        self.barracas_label.setGeometry(QtCore.QRect(20, 440, 141, 16))
        self.barracas_label.setObjectName("barracas_label")
        self.aniversariante_label = QtWidgets.QLabel(Add_Festa)
        self.aniversariante_label.setGeometry(QtCore.QRect(20, 320, 151, 16))
        self.aniversariante_label.setObjectName("aniversariante_label")
        self.aniversariante_lineEdit = QtWidgets.QLineEdit(Add_Festa)
        self.aniversariante_lineEdit.setGeometry(QtCore.QRect(20, 340, 371, 28))
        self.aniversariante_lineEdit.setObjectName("aniversariante_lineEdit")
        self.tema_lineEdit = QtWidgets.QLineEdit(Add_Festa)
        self.tema_lineEdit.setGeometry(QtCore.QRect(20, 400, 371, 28))
        self.tema_lineEdit.setObjectName("tema_lineEdit")
        self.tema_label = QtWidgets.QLabel(Add_Festa)
        self.tema_label.setGeometry(QtCore.QRect(20, 380, 151, 16))
        self.tema_label.setObjectName("tema_label")
        self.faixa_label = QtWidgets.QLabel(Add_Festa)
        self.faixa_label.setGeometry(QtCore.QRect(190, 440, 81, 16))
        self.faixa_label.setObjectName("faixa_label")
        self.faixa_comboBox = QtWidgets.QComboBox(Add_Festa)
        self.faixa_comboBox.setGeometry(QtCore.QRect(190, 460, 121, 28))
        self.faixa_comboBox.setObjectName("faixa_comboBox")
        self.tableWidget = QtWidgets.QTableWidget(Add_Festa)
        self.tableWidget.setGeometry(QtCore.QRect(440, 80, 391, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Add_Festa)
        QtCore.QMetaObject.connectSlotsByName(Add_Festa)

    def retranslateUi(self, Add_Festa):
        _translate = QtCore.QCoreApplication.translate
        Add_Festa.setWindowTitle(_translate("Add_Festa", "Dialog"))
        self.cliente_label.setText(_translate("Add_Festa", "Cliente"))
        self.cliente_pushButton.setText(_translate("Add_Festa", "Adicionar"))
        self.data_label.setText(_translate("Add_Festa", "Data"))
        self.convidados_label.setText(_translate("Add_Festa", "Convidados"))
        self.preco_label.setText(_translate("Add_Festa", "Preço"))
        self.casaDeFesta_label.setText(_translate("Add_Festa", "Casa de Festa"))
        self.casaDeFesta_pushButton.setText(_translate("Add_Festa", "Adicionar"))
        self.gerente_pushButton.setText(_translate("Add_Festa", "Adicionar"))
        self.gerente_label.setText(_translate("Add_Festa", "Gerente"))
        self.bebida_label.setText(_translate("Add_Festa", "Bebida"))
        self.quantidade_pushButton.setText(_translate("Add_Festa", "+"))
        self.quantidade_label.setText(_translate("Add_Festa", "Quantidade"))
        self.barracas_label.setText(_translate("Add_Festa", "Barracas de Raspadinha"))
        self.aniversariante_label.setText(_translate("Add_Festa", "Nome do Aniversariante"))
        self.tema_label.setText(_translate("Add_Festa", "Tema"))
        self.faixa_label.setText(_translate("Add_Festa", "Faixa Etária"))

