# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/festa.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_Festa(object):
    def setupUi(self, Add_Festa):
        Add_Festa.setObjectName("Add_Festa")
        Add_Festa.resize(680, 606)
        self.gridLayout_2 = QtWidgets.QGridLayout(Add_Festa)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Add_Festa)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.cliente_label = QtWidgets.QLabel(self.frame)
        self.cliente_label.setObjectName("cliente_label")
        self.gridLayout.addWidget(self.cliente_label, 0, 0, 1, 1)
        self.bebida_label = QtWidgets.QLabel(self.frame)
        self.bebida_label.setObjectName("bebida_label")
        self.gridLayout.addWidget(self.bebida_label, 0, 3, 1, 1)
        self.quantidade_label = QtWidgets.QLabel(self.frame)
        self.quantidade_label.setObjectName("quantidade_label")
        self.gridLayout.addWidget(self.quantidade_label, 0, 4, 1, 1)
        self.cliente_comboBox = QtWidgets.QComboBox(self.frame)
        self.cliente_comboBox.setObjectName("cliente_comboBox")
        self.gridLayout.addWidget(self.cliente_comboBox, 1, 0, 1, 2)
        self.cliente_pushButton = QtWidgets.QPushButton(self.frame)
        self.cliente_pushButton.setObjectName("cliente_pushButton")
        self.gridLayout.addWidget(self.cliente_pushButton, 1, 2, 1, 1)
        self.bebida_comboBox = QtWidgets.QComboBox(self.frame)
        self.bebida_comboBox.setObjectName("bebida_comboBox")
        self.gridLayout.addWidget(self.bebida_comboBox, 1, 3, 1, 1)
        self.quantidade_spinBox = QtWidgets.QSpinBox(self.frame)
        self.quantidade_spinBox.setMaximum(99999)
        self.quantidade_spinBox.setObjectName("quantidade_spinBox")
        self.gridLayout.addWidget(self.quantidade_spinBox, 1, 4, 1, 1)
        self.bebida_addButton = QtWidgets.QPushButton(self.frame)
        self.bebida_addButton.setObjectName("bebida_addButton")
        self.gridLayout.addWidget(self.bebida_addButton, 1, 5, 1, 1)
        self.data_label = QtWidgets.QLabel(self.frame)
        self.data_label.setObjectName("data_label")
        self.gridLayout.addWidget(self.data_label, 2, 0, 1, 1)
        self.bebidas_tableWidget = QtWidgets.QTableWidget(self.frame)
        self.bebidas_tableWidget.setRowCount(0)
        self.bebidas_tableWidget.setColumnCount(3)
        self.bebidas_tableWidget.setObjectName("bebidas_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.bebidas_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bebidas_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bebidas_tableWidget.setHorizontalHeaderItem(2, item)
        self.bebidas_tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.bebidas_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.bebidas_tableWidget, 2, 3, 4, 3)
        self.data_timeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.data_timeEdit.setObjectName("data_timeEdit")
        self.gridLayout.addWidget(self.data_timeEdit, 3, 0, 1, 3)
        self.convidados_label = QtWidgets.QLabel(self.frame)
        self.convidados_label.setObjectName("convidados_label")
        self.gridLayout.addWidget(self.convidados_label, 4, 0, 1, 1)
        self.preco_label = QtWidgets.QLabel(self.frame)
        self.preco_label.setObjectName("preco_label")
        self.gridLayout.addWidget(self.preco_label, 4, 1, 1, 1)
        self.convidados_spinBox = QtWidgets.QSpinBox(self.frame)
        self.convidados_spinBox.setMaximum(99999)
        self.convidados_spinBox.setObjectName("convidados_spinBox")
        self.gridLayout.addWidget(self.convidados_spinBox, 5, 0, 1, 1)
        self.preco_spinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.preco_spinBox.setMaximum(999999.99)
        self.preco_spinBox.setObjectName("preco_spinBox")
        self.gridLayout.addWidget(self.preco_spinBox, 5, 1, 1, 2)
        self.garcons_label = QtWidgets.QLabel(self.frame)
        self.garcons_label.setObjectName("garcons_label")
        self.gridLayout.addWidget(self.garcons_label, 6, 3, 1, 1)
        self.casaDeFesta_label = QtWidgets.QLabel(self.frame)
        self.casaDeFesta_label.setObjectName("casaDeFesta_label")
        self.gridLayout.addWidget(self.casaDeFesta_label, 7, 0, 1, 1)
        self.garcons_comboBox = QtWidgets.QComboBox(self.frame)
        self.garcons_comboBox.setObjectName("garcons_comboBox")
        self.gridLayout.addWidget(self.garcons_comboBox, 7, 3, 1, 2)
        self.garcons_addButton = QtWidgets.QPushButton(self.frame)
        self.garcons_addButton.setObjectName("garcons_addButton")
        self.gridLayout.addWidget(self.garcons_addButton, 7, 5, 1, 1)
        self.casaDeFesta_comboBox = QtWidgets.QComboBox(self.frame)
        self.casaDeFesta_comboBox.setObjectName("casaDeFesta_comboBox")
        self.gridLayout.addWidget(self.casaDeFesta_comboBox, 8, 0, 1, 2)
        self.casaDeFesta_pushButton = QtWidgets.QPushButton(self.frame)
        self.casaDeFesta_pushButton.setObjectName("casaDeFesta_pushButton")
        self.gridLayout.addWidget(self.casaDeFesta_pushButton, 8, 2, 1, 1)
        self.gerente_label = QtWidgets.QLabel(self.frame)
        self.gerente_label.setObjectName("gerente_label")
        self.gridLayout.addWidget(self.gerente_label, 9, 0, 1, 1)
        self.aniversariante_label = QtWidgets.QLabel(self.frame)
        self.aniversariante_label.setObjectName("aniversariante_label")
        self.gridLayout.addWidget(self.aniversariante_label, 11, 0, 1, 1)
        self.aniversariante_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.aniversariante_lineEdit.setMaxLength(75)
        self.aniversariante_lineEdit.setObjectName("aniversariante_lineEdit")
        self.gridLayout.addWidget(self.aniversariante_lineEdit, 12, 0, 1, 3)
        self.tema_label = QtWidgets.QLabel(self.frame)
        self.tema_label.setObjectName("tema_label")
        self.gridLayout.addWidget(self.tema_label, 13, 0, 1, 1)
        self.tema_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.tema_lineEdit.setMaxLength(30)
        self.tema_lineEdit.setObjectName("tema_lineEdit")
        self.gridLayout.addWidget(self.tema_lineEdit, 14, 0, 1, 3)
        self.barracas_label = QtWidgets.QLabel(self.frame)
        self.barracas_label.setObjectName("barracas_label")
        self.gridLayout.addWidget(self.barracas_label, 15, 0, 1, 1)
        self.faixa_label = QtWidgets.QLabel(self.frame)
        self.faixa_label.setObjectName("faixa_label")
        self.gridLayout.addWidget(self.faixa_label, 15, 2, 1, 1)
        self.barracas_spinBox = QtWidgets.QSpinBox(self.frame)
        self.barracas_spinBox.setMaximum(99999)
        self.barracas_spinBox.setObjectName("barracas_spinBox")
        self.gridLayout.addWidget(self.barracas_spinBox, 16, 0, 1, 2)
        self.faixa_comboBox = QtWidgets.QComboBox(self.frame)
        self.faixa_comboBox.setObjectName("faixa_comboBox")
        self.gridLayout.addWidget(self.faixa_comboBox, 16, 2, 1, 1)
        self.gerente_comboBox = QtWidgets.QComboBox(self.frame)
        self.gerente_comboBox.setObjectName("gerente_comboBox")
        self.gridLayout.addWidget(self.gerente_comboBox, 10, 0, 1, 3)
        self.garcons_tableWidget = QtWidgets.QTableWidget(self.frame)
        self.garcons_tableWidget.setRowCount(0)
        self.garcons_tableWidget.setColumnCount(1)
        self.garcons_tableWidget.setObjectName("garcons_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.garcons_tableWidget.setHorizontalHeaderItem(0, item)
        self.garcons_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.garcons_tableWidget, 8, 3, 4, 3)
        self.operador_label = QtWidgets.QLabel(self.frame)
        self.operador_label.setObjectName("operador_label")
        self.gridLayout.addWidget(self.operador_label, 12, 3, 1, 1)
        self.operador_addButton = QtWidgets.QPushButton(self.frame)
        self.operador_addButton.setObjectName("operador_addButton")
        self.gridLayout.addWidget(self.operador_addButton, 13, 5, 1, 1)
        self.operador_comboBox = QtWidgets.QComboBox(self.frame)
        self.operador_comboBox.setObjectName("operador_comboBox")
        self.gridLayout.addWidget(self.operador_comboBox, 13, 3, 1, 2)
        self.garcons_tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.garcons_tableWidget_2.setRowCount(0)
        self.garcons_tableWidget_2.setColumnCount(1)
        self.garcons_tableWidget_2.setObjectName("garcons_tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.garcons_tableWidget_2.setHorizontalHeaderItem(0, item)
        self.garcons_tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.garcons_tableWidget_2, 14, 3, 3, 3)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(466, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Add_Festa)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(Add_Festa)
        QtCore.QMetaObject.connectSlotsByName(Add_Festa)

    def retranslateUi(self, Add_Festa):
        _translate = QtCore.QCoreApplication.translate
        Add_Festa.setWindowTitle(_translate("Add_Festa", "Dialog"))
        self.cliente_label.setText(_translate("Add_Festa", "Cliente"))
        self.bebida_label.setText(_translate("Add_Festa", "Bebida"))
        self.quantidade_label.setText(_translate("Add_Festa", "Quantidade"))
        self.cliente_pushButton.setText(_translate("Add_Festa", "Adicionar"))
        self.bebida_addButton.setText(_translate("Add_Festa", "+"))
        self.data_label.setText(_translate("Add_Festa", "Data"))
        item = self.bebidas_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Add_Festa", "Nome"))
        item = self.bebidas_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Add_Festa", "Volume"))
        item = self.bebidas_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Add_Festa", "Quantidade"))
        self.convidados_label.setText(_translate("Add_Festa", "Convidados"))
        self.preco_label.setText(_translate("Add_Festa", "Preço"))
        self.garcons_label.setText(_translate("Add_Festa", "Garçons"))
        self.casaDeFesta_label.setText(_translate("Add_Festa", "Casa de Festa"))
        self.garcons_addButton.setText(_translate("Add_Festa", "+"))
        self.casaDeFesta_pushButton.setText(_translate("Add_Festa", "Adicionar"))
        self.gerente_label.setText(_translate("Add_Festa", "Gerente"))
        self.aniversariante_label.setText(_translate("Add_Festa", "Nome do Aniversariante"))
        self.tema_label.setText(_translate("Add_Festa", "Tema"))
        self.barracas_label.setText(_translate("Add_Festa", "Barracas de Raspadinha"))
        self.faixa_label.setText(_translate("Add_Festa", "Faixa Etária"))
        item = self.garcons_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Add_Festa", "Nome"))
        self.operador_label.setText(_translate("Add_Festa", "Operador de Raspadinha"))
        self.operador_addButton.setText(_translate("Add_Festa", "+"))
        item = self.garcons_tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Add_Festa", "Nome"))

