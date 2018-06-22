# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from bebida import Ui_Bebida as Bebida
from casadefesta import Ui_Dialog as CasaDeFesta
from cliente import Ui_Dialog as Cliente
from festa import Ui_Add_Festa as Festa
from fornecedor import Ui_Dialog as Fornecedor
from funcionario import Ui_Funcionario as Funcionario


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("Gerenciador de Festas")
		MainWindow.resize(895, 480)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 401))
		self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
		self.tabWidget.setDocumentMode(False)
		self.tabWidget.setObjectName("tabWidget")
		
		# tab festa
		self.festa = QtWidgets.QWidget()
		self.festa.setObjectName("festa")
		self.festa_addButton = QtWidgets.QPushButton(self.festa)
		self.festa_addButton.setGeometry(QtCore.QRect(690, 330, 92, 34))
		self.festa_addButton.setObjectName("festa_addButton")
		self.data_edit = QtWidgets.QDateEdit(self.festa)
		self.data_edit.setGeometry(QtCore.QRect(10, 30, 141, 28))
		self.data_edit.setObjectName("data_edit")
		self.casaDeFesa_comboBox = QtWidgets.QComboBox(self.festa)
		self.casaDeFesa_comboBox.setGeometry(QtCore.QRect(160, 30, 341, 28))
		self.casaDeFesa_comboBox.setObjectName("casaDeFesa_comboBox")
		self.casaDeFesta_label = QtWidgets.QLabel(self.festa)
		self.casaDeFesta_label.setGeometry(QtCore.QRect(160, 10, 81, 16))
		self.casaDeFesta_label.setObjectName("casaDeFesta_label")
		self.gerente_comboBox = QtWidgets.QComboBox(self.festa)
		self.gerente_comboBox.setGeometry(QtCore.QRect(510, 30, 371, 28))
		self.gerente_comboBox.setObjectName("gerente_comboBox")
		self.gerente_label = QtWidgets.QLabel(self.festa)
		self.gerente_label.setGeometry(QtCore.QRect(510, 10, 81, 16))
		self.gerente_label.setObjectName("gerente_label")
		self.data_label = QtWidgets.QLabel(self.festa)
		self.data_label.setGeometry(QtCore.QRect(10, 10, 58, 16))
		self.data_label.setObjectName("data_label")
		self.festa_tableWidget = QtWidgets.QTableWidget(self.festa)
		self.festa_tableWidget.setGeometry(QtCore.QRect(10, 60, 871, 261))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.festa_tableWidget.sizePolicy().hasHeightForWidth())
		self.festa_tableWidget.setSizePolicy(sizePolicy)
		self.festa_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.festa_tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
		self.festa_tableWidget.setWordWrap(True)
		self.festa_tableWidget.setCornerButtonEnabled(True)
		self.festa_tableWidget.setRowCount(0)
		self.festa_tableWidget.setObjectName("festa_tableWidget")
		self.festa_tableWidget.setColumnCount(7)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.festa_tableWidget.setHorizontalHeaderItem(6, item)
		self.festa_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
		self.festa_tableWidget.horizontalHeader().setDefaultSectionSize(120)
		self.festa_tableWidget.horizontalHeader().setMinimumSectionSize(50)
		self.festa_tableWidget.horizontalHeader().setStretchLastSection(True)
		self.festa_tableWidget.verticalHeader().setVisible(False)
		self.festa_tableWidget.verticalHeader().setDefaultSectionSize(30)
		self.festa_delButton = QtWidgets.QPushButton(self.festa)
		self.festa_delButton.setGeometry(QtCore.QRect(790, 330, 92, 34))
		self.festa_delButton.setObjectName("festa_delButton")
		
		# tab funcionario
		self.funcionario = QtWidgets.QWidget()
		self.funcionario.setObjectName("funcionario")
		self.funcionario_addButton = QtWidgets.QPushButton(self.funcionario)
		self.funcionario_addButton.setGeometry(QtCore.QRect(690, 330, 92, 34))
		self.funcionario_addButton.setObjectName("funcionario_addButton")
		self.bartender_check = QtWidgets.QCheckBox(self.funcionario)
		self.bartender_check.setGeometry(QtCore.QRect(10, 30, 81, 28))
		self.bartender_check.setChecked(True)
		self.bartender_check.setObjectName("bartender_check")
		self.gerente_check = QtWidgets.QCheckBox(self.funcionario)
		self.gerente_check.setGeometry(QtCore.QRect(100, 30, 83, 28))
		self.gerente_check.setChecked(True)
		self.gerente_check.setObjectName("gerente_check")
		self.garcom_check = QtWidgets.QCheckBox(self.funcionario)
		self.garcom_check.setGeometry(QtCore.QRect(180, 30, 83, 28))
		self.garcom_check.setChecked(True)
		self.garcom_check.setObjectName("garcom_check")
		self.operador_check = QtWidgets.QCheckBox(self.funcionario)
		self.operador_check.setGeometry(QtCore.QRect(260, 30, 151, 28))
		self.operador_check.setChecked(True)
		self.operador_check.setObjectName("operador_check")
		self.label = QtWidgets.QLabel(self.funcionario)
		self.label.setGeometry(QtCore.QRect(10, 10, 58, 16))
		self.label.setObjectName("label")
		self.funcionario_tableWidget = QtWidgets.QTableWidget(self.funcionario)
		self.funcionario_tableWidget.setGeometry(QtCore.QRect(10, 60, 871, 261))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.funcionario_tableWidget.sizePolicy().hasHeightForWidth())
		self.funcionario_tableWidget.setSizePolicy(sizePolicy)
		self.funcionario_tableWidget.setWordWrap(True)
		self.funcionario_tableWidget.setCornerButtonEnabled(True)
		self.funcionario_tableWidget.setRowCount(0)
		self.funcionario_tableWidget.setObjectName("funcionario_tableWidget")
		self.funcionario_tableWidget.setColumnCount(7)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.funcionario_tableWidget.setHorizontalHeaderItem(6, item)
		self.funcionario_tableWidget.horizontalHeader().setDefaultSectionSize(120)
		self.funcionario_tableWidget.horizontalHeader().setStretchLastSection(True)
		self.funcionario_tableWidget.verticalHeader().setVisible(False)
		self.funcionario_delButton = QtWidgets.QPushButton(self.funcionario)
		self.funcionario_delButton.setGeometry(QtCore.QRect(790, 330, 92, 34))
		self.funcionario_delButton.setObjectName("funcionario_delButton")
		self.tabWidget.addTab(self.funcionario, "")
		
		self.bebidas = QtWidgets.QWidget()
		self.bebidas.setObjectName("bebidas")
		self.bebida_addButton = QtWidgets.QPushButton(self.bebidas)
		self.bebida_addButton.setGeometry(QtCore.QRect(690, 330, 92, 34))
		self.bebida_addButton.setObjectName("bebida_addButton")
		self.quantidade_spinBox = QtWidgets.QSpinBox(self.bebidas)
		self.quantidade_spinBox.setGeometry(QtCore.QRect(10, 30, 141, 28))
		self.quantidade_spinBox.setObjectName("quantidade_spinBox")
		self.quantidade_label = QtWidgets.QLabel(self.bebidas)
		self.quantidade_label.setGeometry(QtCore.QRect(10, 10, 81, 16))
		self.quantidade_label.setObjectName("quantidade_label")
		self.bebida_tableWidget = QtWidgets.QTableWidget(self.bebidas)
		self.bebida_tableWidget.setGeometry(QtCore.QRect(10, 60, 871, 261))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.bebida_tableWidget.sizePolicy().hasHeightForWidth())
		self.bebida_tableWidget.setSizePolicy(sizePolicy)
		self.bebida_tableWidget.setWordWrap(True)
		self.bebida_tableWidget.setCornerButtonEnabled(True)
		self.bebida_tableWidget.setRowCount(0)
		self.bebida_tableWidget.setObjectName("bebida_tableWidget")
		self.bebida_tableWidget.setColumnCount(3)
		item = QtWidgets.QTableWidgetItem()
		self.bebida_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.bebida_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.bebida_tableWidget.setHorizontalHeaderItem(2, item)
		self.bebida_tableWidget.horizontalHeader().setDefaultSectionSize(250)
		self.bebida_tableWidget.horizontalHeader().setStretchLastSection(True)
		self.bebida_tableWidget.verticalHeader().setVisible(False)
		self.bebida_delButton = QtWidgets.QPushButton(self.bebidas)
		self.bebida_delButton.setGeometry(QtCore.QRect(790, 330, 92, 34))
		self.bebida_delButton.setObjectName("bebida_delButton")
		self.tabWidget.addTab(self.bebidas, "")
		
		self.fornecedores = QtWidgets.QWidget()
		self.fornecedores.setObjectName("fornecedores")
		self.fornecedor_delButton = QtWidgets.QPushButton(self.fornecedores)
		self.fornecedor_delButton.setGeometry(QtCore.QRect(790, 330, 92, 34))
		self.fornecedor_delButton.setObjectName("fornecedor_delButton")
		self.fornecedor_tableWidget = QtWidgets.QTableWidget(self.fornecedores)
		self.fornecedor_tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 311))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.fornecedor_tableWidget.sizePolicy().hasHeightForWidth())
		self.fornecedor_tableWidget.setSizePolicy(sizePolicy)
		self.fornecedor_tableWidget.setWordWrap(True)
		self.fornecedor_tableWidget.setCornerButtonEnabled(True)
		self.fornecedor_tableWidget.setRowCount(0)
		self.fornecedor_tableWidget.setObjectName("fornecedor_tableWidget")
		self.fornecedor_tableWidget.setColumnCount(7)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.fornecedor_tableWidget.setHorizontalHeaderItem(6, item)
		self.fornecedor_tableWidget.horizontalHeader().setDefaultSectionSize(120)
		self.fornecedor_tableWidget.horizontalHeader().setStretchLastSection(True)
		self.fornecedor_tableWidget.verticalHeader().setVisible(False)
		self.fornecedor_addButton = QtWidgets.QPushButton(self.fornecedores)
		self.fornecedor_addButton.setGeometry(QtCore.QRect(690, 330, 92, 34))
		self.fornecedor_addButton.setObjectName("fornecedor_addButton")
		self.tabWidget.addTab(self.fornecedores, "")
		
		self.cliente = QtWidgets.QWidget()
		self.cliente.setObjectName("cliente")
		self.cliente_delButton = QtWidgets.QPushButton(self.cliente)
		self.cliente_delButton.setGeometry(QtCore.QRect(790, 330, 92, 34))
		self.cliente_delButton.setObjectName("cliente_delButton")
		self.cliente_tableWidget = QtWidgets.QTableWidget(self.cliente)
		self.cliente_tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 311))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.cliente_tableWidget.sizePolicy().hasHeightForWidth())
		self.cliente_tableWidget.setSizePolicy(sizePolicy)
		self.cliente_tableWidget.setMidLineWidth(0)
		self.cliente_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.cliente_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.cliente_tableWidget.setWordWrap(True)
		self.cliente_tableWidget.setCornerButtonEnabled(True)
		self.cliente_tableWidget.setRowCount(0)
		self.cliente_tableWidget.setObjectName("cliente_tableWidget")
		self.cliente_tableWidget.setColumnCount(8)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.cliente_tableWidget.setHorizontalHeaderItem(7, item)
		self.cliente_tableWidget.horizontalHeader().setDefaultSectionSize(105)
		self.cliente_tableWidget.horizontalHeader().setStretchLastSection(True)
		self.cliente_tableWidget.verticalHeader().setVisible(False)
		self.cliente_tableWidget.verticalHeader().setHighlightSections(True)
		self.cliente_addButton = QtWidgets.QPushButton(self.cliente)
		self.cliente_addButton.setGeometry(QtCore.QRect(690, 330, 92, 34))
		self.cliente_addButton.setObjectName("cliente_addButton")
		self.tabWidget.addTab(self.cliente, "")
		
		self.casaDeFesta = QtWidgets.QWidget()
		self.casaDeFesta.setObjectName("casaDeFesta")
		self.casaDeFesta_addButton = QtWidgets.QPushButton(self.casaDeFesta)
		self.casaDeFesta_addButton.setGeometry(QtCore.QRect(690, 330, 92, 34))
		self.casaDeFesta_addButton.setObjectName("casaDeFesta_addButton")
		self.casaDeFesta_tableWidget = QtWidgets.QTableWidget(self.casaDeFesta)
		self.casaDeFesta_tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 311))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.casaDeFesta_tableWidget.sizePolicy().hasHeightForWidth())
		self.casaDeFesta_tableWidget.setSizePolicy(sizePolicy)
		self.casaDeFesta_tableWidget.setWordWrap(True)
		self.casaDeFesta_tableWidget.setCornerButtonEnabled(True)
		self.casaDeFesta_tableWidget.setRowCount(0)
		self.casaDeFesta_tableWidget.setObjectName("casaDeFesta_tableWidget")
		self.casaDeFesta_tableWidget.setColumnCount(6)
		item = QtWidgets.QTableWidgetItem()
		self.casaDeFesta_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.casaDeFesta_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.casaDeFesta_tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.casaDeFesta_tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.casaDeFesta_tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.casaDeFesta_tableWidget.setHorizontalHeaderItem(5, item)
		self.casaDeFesta_tableWidget.horizontalHeader().setDefaultSectionSize(140)
		self.casaDeFesta_tableWidget.horizontalHeader().setHighlightSections(True)
		self.casaDeFesta_tableWidget.horizontalHeader().setStretchLastSection(True)
		self.casaDeFesta_tableWidget.verticalHeader().setVisible(False)
		self.casaDeFesta_delButton = QtWidgets.QPushButton(self.casaDeFesta)
		self.casaDeFesta_delButton.setGeometry(QtCore.QRect(790, 330, 92, 34))
		self.casaDeFesta_delButton.setObjectName("casaDeFesta_delButton")
		self.tabWidget.addTab(self.casaDeFesta, "")
		
		self.balanco = QtWidgets.QWidget()
		self.balanco.setObjectName("balanco")
		self.tabWidget.addTab(self.balanco, "")
		
		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 895, 30))
		self.menuBar.setObjectName("menuBar")
		MainWindow.setMenuBar(self.menuBar)
		self.mainToolBar = QtWidgets.QToolBar(MainWindow)
		self.mainToolBar.setObjectName("mainToolBar")
		MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.festa_addButton.setText(_translate("MainWindow", "Adicionar"))
		self.casaDeFesta_label.setText(_translate("MainWindow", "Casa de Festa"))
		self.gerente_label.setText(_translate("MainWindow", "Gerente"))
		self.data_label.setText(_translate("MainWindow", "Data"))
		self.festa_tableWidget.setSortingEnabled(True)
		item = self.festa_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Cliente"))
		item = self.festa_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Data"))
		item = self.festa_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Convidados"))
		item = self.festa_tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Preço"))
		item = self.festa_tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Gerente"))
		item = self.festa_tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Nº de Funcionários"))
		item = self.festa_tableWidget.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Casa de Festa"))
		self.festa_delButton.setText(_translate("MainWindow", "Remover"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.festa), _translate("MainWindow", "Festa"))
		self.funcionario_addButton.setText(_translate("MainWindow", "Adicionar"))
		self.bartender_check.setText(_translate("MainWindow", "Bartender"))
		self.gerente_check.setText(_translate("MainWindow", "Gerente"))
		self.garcom_check.setText(_translate("MainWindow", "Garçom"))
		self.operador_check.setText(_translate("MainWindow", "Operador Raspadinha"))
		self.label.setText(_translate("MainWindow", "Função"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Nome"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Telefone Fixo"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Telefone Móvel"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Cargo"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Comissão"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Local Próx. Festa"))
		item = self.funcionario_tableWidget.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Data Próx. Festa"))
		self.funcionario_delButton.setText(_translate("MainWindow", "Remover"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.funcionario), _translate("MainWindow", "Funcionário"))
		self.bebida_addButton.setText(_translate("MainWindow", "Adicionar"))
		self.quantidade_label.setText(_translate("MainWindow", "Quantidade"))
		item = self.bebida_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Nome"))
		item = self.bebida_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Volume"))
		item = self.bebida_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Quantidade"))
		self.bebida_delButton.setText(_translate("MainWindow", "Remover"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.bebidas), _translate("MainWindow", "Bebidas"))
		self.fornecedor_delButton.setText(_translate("MainWindow", "Remover"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Nome"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "CNPJ"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Telefone"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Banco"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Agência"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Número Conta"))
		item = self.fornecedor_tableWidget.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Tipo da Conta"))
		self.fornecedor_addButton.setText(_translate("MainWindow", "Adicionar"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.fornecedores), _translate("MainWindow", "Fornecedores"))
		self.cliente_delButton.setText(_translate("MainWindow", "Remover"))
		item = self.cliente_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Nome"))
		item = self.cliente_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "CPF"))
		item = self.cliente_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Telefone"))
		item = self.cliente_tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Banco"))
		item = self.cliente_tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Agência"))
		item = self.cliente_tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Nº Conta"))
		item = self.cliente_tableWidget.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Tipo da Conta"))
		item = self.cliente_tableWidget.horizontalHeaderItem(7)
		item.setText(_translate("MainWindow", "Nº de Festas"))
		self.cliente_addButton.setText(_translate("MainWindow", "Adicionar"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.cliente), _translate("MainWindow", "Cliente"))
		self.casaDeFesta_addButton.setText(_translate("MainWindow", "Adicionar"))
		item = self.casaDeFesta_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Nome"))
		item = self.casaDeFesta_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Rua"))
		item = self.casaDeFesta_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Número"))
		item = self.casaDeFesta_tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Cidade"))
		item = self.casaDeFesta_tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "CEP"))
		item = self.casaDeFesta_tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Data Próxima Festa"))
		self.casaDeFesta_delButton.setText(_translate("MainWindow", "Remove"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.casaDeFesta), _translate("MainWindow", "Casa de Festa"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.balanco), _translate("MainWindow", "Balanço"))


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())