# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 480)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_7.setContentsMargins(4, 4, 4, 16)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.festa = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.festa.sizePolicy().hasHeightForWidth())
        self.festa.setSizePolicy(sizePolicy)
        self.festa.setObjectName("festa")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.festa)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget = QtWidgets.QWidget(self.festa)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dataFinal_dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dataFinal_dateEdit.setObjectName("dataFinal_dateEdit")
        self.gridLayout_4.addWidget(self.dataFinal_dateEdit, 1, 1, 1, 1)
        self.gerente_label = QtWidgets.QLabel(self.widget)
        self.gerente_label.setObjectName("gerente_label")
        self.gridLayout_4.addWidget(self.gerente_label, 0, 3, 1, 1)
        self.casaDeFesta_label = QtWidgets.QLabel(self.widget)
        self.casaDeFesta_label.setObjectName("casaDeFesta_label")
        self.gridLayout_4.addWidget(self.casaDeFesta_label, 0, 2, 1, 1)
        self.data_label = QtWidgets.QLabel(self.widget)
        self.data_label.setObjectName("data_label")
        self.gridLayout_4.addWidget(self.data_label, 0, 1, 1, 1)
        self.gerente_comboBox = QtWidgets.QComboBox(self.widget)
        self.gerente_comboBox.setObjectName("gerente_comboBox")
        self.gridLayout_4.addWidget(self.gerente_comboBox, 1, 3, 1, 1)
        self.casaDeFesta_comboBox = QtWidgets.QComboBox(self.widget)
        self.casaDeFesta_comboBox.setObjectName("casaDeFesta_comboBox")
        self.gridLayout_4.addWidget(self.casaDeFesta_comboBox, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.dataInicial_dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dataInicial_dateEdit.setCalendarPopup(False)
        self.dataInicial_dateEdit.setObjectName("dataInicial_dateEdit")
        self.gridLayout_4.addWidget(self.dataInicial_dateEdit, 1, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 3)
        self.gridLayout_4.setColumnStretch(3, 3)
        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 2)
        self.festa_tableWidget = QtWidgets.QTableWidget(self.festa)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.festa_tableWidget.sizePolicy().hasHeightForWidth())
        self.festa_tableWidget.setSizePolicy(sizePolicy)
        self.festa_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.festa_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.festa_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.festa_tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.festa_tableWidget.setWordWrap(True)
        self.festa_tableWidget.setCornerButtonEnabled(True)
        self.festa_tableWidget.setRowCount(0)
        self.festa_tableWidget.setObjectName("festa_tableWidget")
        self.festa_tableWidget.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        self.festa_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.festa_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.festa_tableWidget.setHorizontalHeaderItem(9, item)
        self.festa_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.festa_tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.festa_tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.festa_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.festa_tableWidget.verticalHeader().setVisible(False)
        self.festa_tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_5.addWidget(self.festa_tableWidget, 1, 0, 1, 2)
        self.festa_addButton = QtWidgets.QPushButton(self.festa)
        self.festa_addButton.setObjectName("festa_addButton")
        self.gridLayout_5.addWidget(self.festa_addButton, 2, 0, 1, 1)
        self.festa_delButton = QtWidgets.QPushButton(self.festa)
        self.festa_delButton.setObjectName("festa_delButton")
        self.gridLayout_5.addWidget(self.festa_delButton, 2, 1, 1, 1)
        self.tabWidget.addTab(self.festa, "")
        self.funcionario = QtWidgets.QWidget()
        self.funcionario.setObjectName("funcionario")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.funcionario)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.widget_2 = QtWidgets.QWidget(self.funcionario)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_6.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.garcom_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.garcom_radioButton.setObjectName("garcom_radioButton")
        self.gridLayout_6.addWidget(self.garcom_radioButton, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(526, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 3, 1, 1)
        self.gerente_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.gerente_radioButton.setChecked(True)
        self.gerente_radioButton.setObjectName("gerente_radioButton")
        self.gridLayout_6.addWidget(self.gerente_radioButton, 1, 0, 1, 1)
        self.operador_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.operador_radioButton.setObjectName("operador_radioButton")
        self.gridLayout_6.addWidget(self.operador_radioButton, 1, 2, 1, 1)
        self.gridLayout_8.addWidget(self.widget_2, 0, 0, 1, 2)
        self.funcionario_delButton = QtWidgets.QPushButton(self.funcionario)
        self.funcionario_delButton.setObjectName("funcionario_delButton")
        self.gridLayout_8.addWidget(self.funcionario_delButton, 2, 1, 1, 1)
        self.funcionario_addButton = QtWidgets.QPushButton(self.funcionario)
        self.funcionario_addButton.setObjectName("funcionario_addButton")
        self.gridLayout_8.addWidget(self.funcionario_addButton, 2, 0, 1, 1)
        self.funcionario_tableWidget = QtWidgets.QTableWidget(self.funcionario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcionario_tableWidget.sizePolicy().hasHeightForWidth())
        self.funcionario_tableWidget.setSizePolicy(sizePolicy)
        self.funcionario_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.funcionario_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.gridLayout_8.addWidget(self.funcionario_tableWidget, 1, 0, 1, 2)
        self.tabWidget.addTab(self.funcionario, "")
        self.bebidas = QtWidgets.QWidget()
        self.bebidas.setObjectName("bebidas")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.bebidas)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.quantidadeMin_label = QtWidgets.QLabel(self.bebidas)
        self.quantidadeMin_label.setObjectName("quantidadeMin_label")
        self.gridLayout_9.addWidget(self.quantidadeMin_label, 0, 0, 1, 1)
        self.quantidadeMin_spinBox = QtWidgets.QSpinBox(self.bebidas)
        self.quantidadeMin_spinBox.setMaximum(99998)
        self.quantidadeMin_spinBox.setObjectName("quantidadeMin_spinBox")
        self.gridLayout_9.addWidget(self.quantidadeMin_spinBox, 1, 0, 1, 1)
        self.quantidadeMax_label = QtWidgets.QLabel(self.bebidas)
        self.quantidadeMax_label.setObjectName("quantidadeMax_label")
        self.gridLayout_9.addWidget(self.quantidadeMax_label, 0, 1, 1, 1)
        self.bebida_addButton = QtWidgets.QPushButton(self.bebidas)
        self.bebida_addButton.setObjectName("bebida_addButton")
        self.gridLayout_9.addWidget(self.bebida_addButton, 3, 0, 1, 1)
        self.bebida_tableWidget = QtWidgets.QTableWidget(self.bebidas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bebida_tableWidget.sizePolicy().hasHeightForWidth())
        self.bebida_tableWidget.setSizePolicy(sizePolicy)
        self.bebida_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.bebida_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.gridLayout_9.addWidget(self.bebida_tableWidget, 2, 0, 1, 2)
        self.bebida_delButton = QtWidgets.QPushButton(self.bebidas)
        self.bebida_delButton.setObjectName("bebida_delButton")
        self.gridLayout_9.addWidget(self.bebida_delButton, 3, 1, 1, 1)
        self.quantidadeMax_spinBox = QtWidgets.QSpinBox(self.bebidas)
        self.quantidadeMax_spinBox.setMinimum(1)
        self.quantidadeMax_spinBox.setMaximum(99999)
        self.quantidadeMax_spinBox.setProperty("value", 99999)
        self.quantidadeMax_spinBox.setObjectName("quantidadeMax_spinBox")
        self.gridLayout_9.addWidget(self.quantidadeMax_spinBox, 1, 1, 1, 1)
        self.tabWidget.addTab(self.bebidas, "")
        self.fornecedores = QtWidgets.QWidget()
        self.fornecedores.setObjectName("fornecedores")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.fornecedores)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.fornecedor_tableWidget = QtWidgets.QTableWidget(self.fornecedores)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fornecedor_tableWidget.sizePolicy().hasHeightForWidth())
        self.fornecedor_tableWidget.setSizePolicy(sizePolicy)
        self.fornecedor_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.fornecedor_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.gridLayout_10.addWidget(self.fornecedor_tableWidget, 0, 0, 1, 2)
        self.fornecedor_addButton = QtWidgets.QPushButton(self.fornecedores)
        self.fornecedor_addButton.setObjectName("fornecedor_addButton")
        self.gridLayout_10.addWidget(self.fornecedor_addButton, 1, 0, 1, 1)
        self.fornecedor_delButton = QtWidgets.QPushButton(self.fornecedores)
        self.fornecedor_delButton.setObjectName("fornecedor_delButton")
        self.gridLayout_10.addWidget(self.fornecedor_delButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.fornecedores, "")
        self.cliente = QtWidgets.QWidget()
        self.cliente.setObjectName("cliente")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.cliente)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.cliente_tableWidget = QtWidgets.QTableWidget(self.cliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cliente_tableWidget.sizePolicy().hasHeightForWidth())
        self.cliente_tableWidget.setSizePolicy(sizePolicy)
        self.cliente_tableWidget.setMidLineWidth(0)
        self.cliente_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cliente_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cliente_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cliente_tableWidget.setWordWrap(True)
        self.cliente_tableWidget.setCornerButtonEnabled(True)
        self.cliente_tableWidget.setRowCount(0)
        self.cliente_tableWidget.setObjectName("cliente_tableWidget")
        self.cliente_tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.cliente_tableWidget.setHorizontalHeaderItem(8, item)
        self.cliente_tableWidget.horizontalHeader().setDefaultSectionSize(105)
        self.cliente_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.cliente_tableWidget.verticalHeader().setVisible(False)
        self.cliente_tableWidget.verticalHeader().setHighlightSections(True)
        self.gridLayout_11.addWidget(self.cliente_tableWidget, 0, 0, 1, 2)
        self.cliente_addButton = QtWidgets.QPushButton(self.cliente)
        self.cliente_addButton.setObjectName("cliente_addButton")
        self.gridLayout_11.addWidget(self.cliente_addButton, 1, 0, 1, 1)
        self.cliente_delButton = QtWidgets.QPushButton(self.cliente)
        self.cliente_delButton.setObjectName("cliente_delButton")
        self.gridLayout_11.addWidget(self.cliente_delButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.cliente, "")
        self.casaDeFesta = QtWidgets.QWidget()
        self.casaDeFesta.setObjectName("casaDeFesta")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.casaDeFesta)
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.casaDeFesta_tableWidget = QtWidgets.QTableWidget(self.casaDeFesta)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.casaDeFesta_tableWidget.sizePolicy().hasHeightForWidth())
        self.casaDeFesta_tableWidget.setSizePolicy(sizePolicy)
        self.casaDeFesta_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.casaDeFesta_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.gridLayout_12.addWidget(self.casaDeFesta_tableWidget, 0, 0, 1, 2)
        self.casaDeFesta_addButton = QtWidgets.QPushButton(self.casaDeFesta)
        self.casaDeFesta_addButton.setObjectName("casaDeFesta_addButton")
        self.gridLayout_12.addWidget(self.casaDeFesta_addButton, 1, 0, 1, 1)
        self.casaDeFesta_delButton = QtWidgets.QPushButton(self.casaDeFesta)
        self.casaDeFesta_delButton.setObjectName("casaDeFesta_delButton")
        self.gridLayout_12.addWidget(self.casaDeFesta_delButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.casaDeFesta, "")
        self.balanco = QtWidgets.QWidget()
        self.balanco.setObjectName("balanco")
        self.tabWidget.addTab(self.balanco, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dataFinal_dateEdit, self.casaDeFesta_comboBox)
        MainWindow.setTabOrder(self.casaDeFesta_comboBox, self.gerente_comboBox)
        MainWindow.setTabOrder(self.gerente_comboBox, self.festa_tableWidget)
        MainWindow.setTabOrder(self.festa_tableWidget, self.festa_addButton)
        MainWindow.setTabOrder(self.festa_addButton, self.festa_delButton)
        MainWindow.setTabOrder(self.festa_delButton, self.funcionario_tableWidget)
        MainWindow.setTabOrder(self.funcionario_tableWidget, self.funcionario_addButton)
        MainWindow.setTabOrder(self.funcionario_addButton, self.funcionario_delButton)
        MainWindow.setTabOrder(self.funcionario_delButton, self.quantidadeMin_spinBox)
        MainWindow.setTabOrder(self.quantidadeMin_spinBox, self.bebida_tableWidget)
        MainWindow.setTabOrder(self.bebida_tableWidget, self.bebida_addButton)
        MainWindow.setTabOrder(self.bebida_addButton, self.bebida_delButton)
        MainWindow.setTabOrder(self.bebida_delButton, self.fornecedor_tableWidget)
        MainWindow.setTabOrder(self.fornecedor_tableWidget, self.fornecedor_addButton)
        MainWindow.setTabOrder(self.fornecedor_addButton, self.fornecedor_delButton)
        MainWindow.setTabOrder(self.fornecedor_delButton, self.cliente_tableWidget)
        MainWindow.setTabOrder(self.cliente_tableWidget, self.cliente_addButton)
        MainWindow.setTabOrder(self.cliente_addButton, self.cliente_delButton)
        MainWindow.setTabOrder(self.cliente_delButton, self.casaDeFesta_tableWidget)
        MainWindow.setTabOrder(self.casaDeFesta_tableWidget, self.casaDeFesta_addButton)
        MainWindow.setTabOrder(self.casaDeFesta_addButton, self.casaDeFesta_delButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gerente_label.setText(_translate("MainWindow", "Gerente"))
        self.casaDeFesta_label.setText(_translate("MainWindow", "Casa de Festa"))
        self.data_label.setText(_translate("MainWindow", "Data Final"))
        self.label_2.setText(_translate("MainWindow", "Data Inicial"))
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
        item.setText(_translate("MainWindow", "Casa de Festa"))
        item = self.festa_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Nome do Aniversariante"))
        item = self.festa_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tema"))
        item = self.festa_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Faixa Etária"))
        item = self.festa_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Nº de Garçons"))
        self.festa_addButton.setText(_translate("MainWindow", "Adicionar"))
        self.festa_delButton.setText(_translate("MainWindow", "Remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.festa), _translate("MainWindow", "Festas"))
        self.garcom_radioButton.setText(_translate("MainWindow", "Garçom"))
        self.label.setText(_translate("MainWindow", "Função"))
        self.gerente_radioButton.setText(_translate("MainWindow", "Gerente"))
        self.operador_radioButton.setText(_translate("MainWindow", "Operador de Raspadinha"))
        self.funcionario_delButton.setText(_translate("MainWindow", "Remover"))
        self.funcionario_addButton.setText(_translate("MainWindow", "Adicionar"))
        self.funcionario_tableWidget.setSortingEnabled(True)
        item = self.funcionario_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.funcionario_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.funcionario_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefone Fixo"))
        item = self.funcionario_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefone Móvel"))
        item = self.funcionario_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Comissão"))
        item = self.funcionario_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Local Próx. Festa"))
        item = self.funcionario_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Data Próx. Festa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.funcionario), _translate("MainWindow", "Funcionários"))
        self.quantidadeMin_label.setText(_translate("MainWindow", "Quantidade Mínima"))
        self.quantidadeMax_label.setText(_translate("MainWindow", "Quantidade Máxima"))
        self.bebida_addButton.setText(_translate("MainWindow", "Adicionar"))
        self.bebida_tableWidget.setSortingEnabled(True)
        item = self.bebida_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.bebida_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Volume"))
        item = self.bebida_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantidade"))
        self.bebida_delButton.setText(_translate("MainWindow", "Remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bebidas), _translate("MainWindow", "Bebidas"))
        self.fornecedor_tableWidget.setSortingEnabled(True)
        item = self.fornecedor_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CNPJ"))
        item = self.fornecedor_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
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
        self.fornecedor_delButton.setText(_translate("MainWindow", "Remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fornecedores), _translate("MainWindow", "Fornecedores"))
        self.cliente_tableWidget.setSortingEnabled(True)
        item = self.cliente_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.cliente_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.cliente_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefone Fixo"))
        item = self.cliente_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefone Movel"))
        item = self.cliente_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Banco"))
        item = self.cliente_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Agência"))
        item = self.cliente_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Nº Conta"))
        item = self.cliente_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tipo da Conta"))
        item = self.cliente_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Nº de Festas"))
        self.cliente_addButton.setText(_translate("MainWindow", "Adicionar"))
        self.cliente_delButton.setText(_translate("MainWindow", "Remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cliente), _translate("MainWindow", "Clientes"))
        self.casaDeFesta_tableWidget.setSortingEnabled(True)
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
        self.casaDeFesta_addButton.setText(_translate("MainWindow", "Adicionar"))
        self.casaDeFesta_delButton.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.casaDeFesta), _translate("MainWindow", "Casas de Festa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.balanco), _translate("MainWindow", "Balanço"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

