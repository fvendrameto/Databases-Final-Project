from PyQt5 import QtGui, QtCore, QtWidgets # Import the PyQt5 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import csv
import os
import time
from datetime import datetime

from mainwindow import Ui_MainWindow as MainWindow
from bebida import Ui_Bebida as Bebida
from casadefesta import Ui_Dialog as CasaDeFesta
from cliente import Ui_Dialog as Cliente
from festa import Ui_Add_Festa as Festa
from fornecedor import Ui_Dialog as Fornecedor
from funcionario import Ui_Funcionario as Funcionario
from database.dbHelper import dbHelper
from static import bancos, estados

class MainApp(QtWidgets.QMainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.mainwindow = MainWindow()
		self.mainwindow.setupUi(self)
		
		self.dbHelper = dbHelper('grad.icmc.usp.br', 15215, 'orcl', 'G9763193', '9763193')

		self.bebida = Bebida()
		self.casaDeFesta = CasaDeFesta()
		self.cliente = Cliente()
		self.festa = Festa()
		self.fornecedor = Fornecedor()
		self.funcionario = Funcionario()

		self.mainwindow.dataInicial_dateEdit.setDate(QtCore.QDate.currentDate())
		self.mainwindow.dataFinal_dateEdit.setDate(QtCore.QDate.currentDate().addMonths(6))

		self.mainwindow.casaDeFesta_comboBox.addItem('Todas')
		nomeCasasDeFesta = self.dbHelper.getNomeCasasFesta()
		for i, casaDeFesta in enumerate(nomeCasasDeFesta):
			self.mainwindow.casaDeFesta_comboBox.addItem(casaDeFesta[0])

		self.gerentes = {'Todos': 'Todos'}
		self.mainwindow.gerente_comboBox.addItem('Todos')
		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.gerentes[funcionario[1]] = funcionario[0]
			self.mainwindow.gerente_comboBox.addItem(funcionario[1])

		self.mainwindow.festa_addButton.clicked.connect(self.on_festa_addBtn_clicked)
		self.mainwindow.festa_delButton.clicked.connect(self.on_festa_delBtn_clicked)
		self.mainwindow.funcionario_addButton.clicked.connect(self.on_funcionario_addBtn_clicked)
		self.mainwindow.funcionario_delButton.clicked.connect(self.on_funcionario_delBtn_clicked)
		self.mainwindow.bebida_addButton.clicked.connect(self.on_bebida_addBtn_clicked)
		self.mainwindow.bebida_delButton.clicked.connect(self.on_bebida_delBtn_clicked)
		self.mainwindow.fornecedor_addButton.clicked.connect(self.on_fornecedor_addBtn_clicked)
		self.mainwindow.fornecedor_delButton.clicked.connect(self.on_fornecedor_delBtn_clicked)
		self.mainwindow.cliente_addButton.clicked.connect(self.on_cliente_addBtn_clicked)
		self.mainwindow.cliente_delButton.clicked.connect(self.on_cliente_delBtn_clicked)
		self.mainwindow.casaDeFesta_addButton.clicked.connect(self.on_casaDeFesta_addBtn_clicked)
		self.mainwindow.casaDeFesta_delButton.clicked.connect(self.on_casaDeFesta_delBtn_clicked)
		self.mainwindow.gerente_radioButton.clicked.connect(self.searchFuncionarios)
		self.mainwindow.garcom_radioButton.clicked.connect(self.searchFuncionarios)
		self.mainwindow.operador_radioButton.clicked.connect(self.searchFuncionarios)
		self.mainwindow.quantidadeMin_spinBox.valueChanged.connect(self.spinBoxLimit)
		self.mainwindow.quantidadeMax_spinBox.valueChanged.connect(self.searchBebidas)
		self.mainwindow.dataInicial_dateEdit.dateChanged.connect(self.searchFestas)
		self.mainwindow.dataFinal_dateEdit.dateChanged.connect(self.searchFestas)
		self.mainwindow.casaDeFesta_comboBox.currentIndexChanged.connect(self.searchFestas)
		self.mainwindow.gerente_comboBox.currentIndexChanged.connect(self.searchFestas)
		self.mainwindow.festa_tableWidget.cellDoubleClicked.connect(self.editFesta)
		self.mainwindow.funcionario_tableWidget.cellDoubleClicked.connect(self.editFuncionario)
		self.mainwindow.bebida_tableWidget.cellDoubleClicked.connect(self.editBebida)
		self.mainwindow.fornecedor_tableWidget.cellDoubleClicked.connect(self.editFornecedor)

		for i in range(self.mainwindow.festa_tableWidget.columnCount()):
			self.mainwindow.festa_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.mainwindow.funcionario_tableWidget.columnCount()):
			self.mainwindow.funcionario_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.mainwindow.bebida_tableWidget.columnCount()):
			self.mainwindow.bebida_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.mainwindow.fornecedor_tableWidget.columnCount()):
			self.mainwindow.fornecedor_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.mainwindow.cliente_tableWidget.columnCount()):
			self.mainwindow.cliente_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.mainwindow.casaDeFesta_tableWidget.columnCount()):
			self.mainwindow.casaDeFesta_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

		self.searchFestas()
		self.searchFuncionarios()
		self.searchBebidas()
		self.fillFornecedores()
		self.fillClientes()
		self.fillCasasDeFesta()

	def spinBoxLimit(self):
		self.mainwindow.quantidadeMax_spinBox.setMinimum(self.mainwindow.quantidadeMin_spinBox.value()+1)
		self.searchBebidas()

	def searchFestas(self):
		self.mainwindow.festa_tableWidget.clearContents()
		self.mainwindow.festa_tableWidget.setRowCount(0)
		
		self.fillFestas(self.mainwindow.dataInicial_dateEdit.date().toPyDate(), self.mainwindow.dataFinal_dateEdit.date().toPyDate(), self.mainwindow.gerente_comboBox.currentText(), self.mainwindow.casaDeFesta_comboBox.currentText())

	def searchFuncionarios(self):
		self.mainwindow.funcionario_tableWidget.clearContents()
		self.mainwindow.funcionario_tableWidget.setRowCount(0)

		if self.mainwindow.gerente_radioButton.isChecked():
			self.fillFuncionarioGerentes()
		elif self.mainwindow.garcom_radioButton.isChecked():
			self.fillFuncionarioGarcons()
		else:
			self.fillFuncionarioOperadores()

	def searchBebidas(self):
		self.mainwindow.bebida_tableWidget.clearContents()
		self.mainwindow.bebida_tableWidget.setRowCount(0)
		
		self.fillBebidas(self.mainwindow.quantidadeMin_spinBox.value(), self.mainwindow.quantidadeMax_spinBox.value())

	def fillFestas(self, dataInicio, dataFinal, gerente, casaDeFesta):
		allFesta = self.dbHelper.getAllAniversarios(dataInicio, dataFinal, self.gerentes[gerente], casaDeFesta)
		for i, festa in enumerate(allFesta):
			self.mainwindow.festa_tableWidget.insertRow(i)
			for j in range(self.mainwindow.festa_tableWidget.columnCount()):
				self.mainwindow.festa_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(festa[j]))

	def fillFuncionarioGerentes(self):
		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.funcionario_tableWidget.insertRow(i)
			for j in range(self.mainwindow.funcionario_tableWidget.columnCount()):
				self.mainwindow.funcionario_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(funcionario[j]))

	def fillFuncionarioGarcons(self):
		allFuncionario = self.dbHelper.getAllGarcons()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.funcionario_tableWidget.insertRow(i)
			for j in range(self.mainwindow.funcionario_tableWidget.columnCount()):
				self.mainwindow.funcionario_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(funcionario[j]))

	def fillFuncionarioOperadores(self):
		allFuncionario = self.dbHelper.getAllOperadores()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.funcionario_tableWidget.insertRow(i)
			for j in range(self.mainwindow.funcionario_tableWidget.columnCount()):
				self.mainwindow.funcionario_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(funcionario[j]))

	def fillBebidas(self, minimum, maximum):
		allBebida = self.dbHelper.getBebidasInInterval(minimum, maximum)
		for i, bebida in enumerate(allBebida):
			self.mainwindow.bebida_tableWidget.insertRow(i)
			for j in range(self.mainwindow.bebida_tableWidget.columnCount()):
				self.mainwindow.bebida_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(bebida[j]))

	def fillFornecedores(self):
		allFornecedor = self.dbHelper.getAllFornecedores()
		for i, fornecedor in enumerate(allFornecedor):
			self.mainwindow.fornecedor_tableWidget.insertRow(i)
			for j in range(self.mainwindow.fornecedor_tableWidget.columnCount()):
				self.mainwindow.fornecedor_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(fornecedor[j]))

	def fillClientes(self):
		allCliente = self.dbHelper.getAllClientes()
		for i, cliente in enumerate(allCliente):
			self.mainwindow.cliente_tableWidget.insertRow(i)
			for j in range(self.mainwindow.cliente_tableWidget.columnCount()):
				self.mainwindow.cliente_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(cliente[j]))

	def fillCasasDeFesta(self):
		allCasaDeFesta = self.dbHelper.getAllCasasFesta()
		for i, casaDeFesta in enumerate(allCasaDeFesta):
			self.mainwindow.casaDeFesta_tableWidget.insertRow(i)
			for j in range(self.mainwindow.casaDeFesta_tableWidget.columnCount()):
				self.mainwindow.casaDeFesta_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(casaDeFesta[j]))

	def setupFesta(self):
		festa_addDialog = QtWidgets.QDialog()
		self.festa.setupUi(festa_addDialog)

		allCliente = self.dbHelper.getAllClientes()
		for i, cliente in enumerate(allCliente):
			self.festa.cliente_comboBox.addItem(cliente[0])

		nomeCasasDeFesta = self.dbHelper.getNomeCasasFesta()
		for i, casaDeFesta in enumerate(nomeCasasDeFesta):
			self.festa.casaDeFesta_comboBox.addItem(casaDeFesta[0])

		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.festa.gerente_comboBox.addItem(funcionario[0])
		
		self.festa.buttonBox.rejected.connect(lambda : festa_addDialog.close())
		
		self.festa.cliente_pushButton.clicked.connect(self.on_cliente_addBtn_clicked)
		self.festa.casaDeFesta_pushButton.clicked.connect(self.on_casaDeFesta_addBtn_clicked)

		self.festa.bebida_addButton.clicked.connect(self.on_bebida_addToTableBtn_clicked)
		self.festa.garcons_addButton.clicked.connect(self.on_garcons_addToTableBtn_clicked)
		self.festa.operador_addButton.clicked.connect(self.on_operador_addToTableBtn_clicked)

		return festa_addDialog

	def on_festa_addBtn_clicked(self):
		festa_addDialog = self.setupFesta()

		self.festa.buttonBox.accepted.connect(lambda : self.save_festa_and_close(festa_addDialog))

		festa_addDialog.exec_()

	def on_festa_delBtn_clicked(self):
		selectedRow = self.mainwindow.festa_tableWidget.selectedItems()
		
		self.dbHelper.delete('FESTA', ['CLIENTE', 'DATA'], [selectedRow[0].text(), datetime.strptime(selectedRow[1].text(), '%d/%m/%Y')])

		self.searchFestas()

	def save_festa_and_close(self, festa_addDialog):
		# Data a ser salva:
		data = self.festa.data_timeEdit.dateTime().toString()

		# SpinBox a serem salvos:
		convidados = self.festa.convidados_spinBox.value()
		preco = self.festa.preco_spinBox.value()
		barracas = self.festa.barracas_spinBox.value()

		# Itens de ComboBox a serem salvos:
		faixa = self.festa.faixa_comboBox.currentText()
		cliente = self.festa.cliente_comboBox.currentText()
		casaDeFesta = self.festa.casaDeFesta_comboBox.currentText()
		gerente = self.festa.gerente_comboBox.currentText()

		# LineEdits a serem salvos:
		aniversariante = self.festa.aniversariante_lineEdit.text()
		tema = self.festa.tema_lineEdit.text()

		print(self.dbHelper.insertIntoFesta([cliente, data, convidados, 'A', preco, casaDeFesta, gerente]))
		print(self.dbHelper.insertIntoAniversatio([cliente, data, aniversariante, tema, faixa]))

		self.searchFestas()

		festa_addDialog.close()

	def editFesta(self):
		festa_addDialog = self.setupFesta()

		self.festa.buttonBox.accepted.connect(lambda : edit_festa_and_close(festa_addDialog))
		self.festa.buttonBox.rejected.connect(lambda : festa_addDialog.close())

		selectedRow = self.mainwindow.festa_tableWidget.selectedItems()
		self.festa.cliente_comboBox.setCurrentIndex(self.festa.cliente_comboBox.findText(selectedRow[0].text()))
		self.festa.data_timeEdit.setDate(datetime.strptime(selectedRow[1].text(), '%d/%m/%Y'))
		self.festa.convidados_spinBox.setValue(int(selectedRow[2].text()))
		self.festa.preco_spinBox.setValue(float(selectedRow[3].text()))
		self.festa.gerente_comboBox.setCurrentIndex(self.festa.gerente_comboBox.findText(selectedRow[4].text()))
		self.festa.casaDeFesta_comboBox.setCurrentIndex(self.festa.casaDeFesta_comboBox.findText(selectedRow[5].text()))
		self.festa.aniversariante_lineEdit.setText(selectedRow[6].text())
		self.festa.tema_lineEdit.setText(selectedRow[7].text())

		festa_addDialog.exec_()

	def edit_festa_and_close(self, festa_addDialog):
		# Data a ser salva:
		data = self.festa.data_timeEdit.dateTime().toString()

		# SpinBox a serem salvos:
		convidados = self.festa.convidados_spinBox.value()
		preco = self.festa.preco_spinBox.value()
		barracas = self.festa.barracas_spinBox.value()

		# Itens de ComboBox a serem salvos:
		faixa = self.festa.faixa_comboBox.currentText()
		cliente = self.festa.cliente_comboBox.currentText()
		casaDeFesta = self.festa.casaDeFesta_comboBox.currentText()
		gerente = self.festa.gerente_comboBox.currentText()

		# LineEdits a serem salvos:
		aniversariante = self.festa.aniversariante_lineEdit.text()
		tema = self.festa.tema_lineEdit.text()

		print(self.dbHelper.insertIntoFesta([cliente, data], [convidados, 'A', preco, casaDeFesta, gerente]))
		print(self.dbHelper.insertIntoAniversatio([cliente, data], [aniversariante, tema, faixa]))

		festa_addDialog.close()

	def setupFuncionario(self):
		funcionario_addDialog = QtWidgets.QDialog()
		self.funcionario.setupUi(funcionario_addDialog)

		self.funcionario.cargo_comboBox.addItem('Gerente')
		self.funcionario.cargo_comboBox.addItem('Garçom')
		self.funcionario.cargo_comboBox.addItem('Operador')

		self.funcionario.buttonBox.rejected.connect(lambda : funcionario_addDialog.close())

		return funcionario_addDialog

	def on_funcionario_addBtn_clicked(self):
		funcionario_addDialog = self.setupFuncionario()

		self.funcionario.buttonBox.accepted.connect(lambda : self.save_funcionario_and_close(funcionario_addDialog))

		funcionario_addDialog.exec_()

	def on_funcionario_delBtn_clicked(self):
		selectedRow = self.mainwindow.funcionario_tableWidget.selectedItems()
		
		self.dbHelper.delete('FUNCIONARIO', ['CPF'], [selectedRow[0].text()])
		
		self.searchFuncionarios()

	def save_funcionario_and_close(self, funcionario_addDialog):
		nome = self.funcionario.nome_lineEdit.text()
		cpf = self.funcionario.cpf_lineEdit.text()
		telFixo = self.funcionario.telFixo_lineEdit.text()
		telMovel = self.funcionario.telMovel_lineEdit.text()

		comissao = self.funcionario.comissao_spinBox.value()

		cargo = self.funcionario.cargo_comboBox.currentText()

		print(self.dbHelper.insertIntoFuncionario([cpf, nome, telFixo, telMovel, comissao, cargo]))

		if cargo == 'Gerente':
			self.gerentes[nome] = cpf
			self.mainwindow.gerente_comboBox.addItem(nome)

		self.searchFuncionarios()

		funcionario_addDialog.close()

	def editFuncionario(self):
		funcionario_addDialog = self.setupFuncionario()

		# TODO edit_funcionario_and_close
		self.funcionario.buttonBox.accepted.connect(lambda : print('oi'))

		selectedRow = self.mainwindow.funcionario_tableWidget.selectedItems()
		self.funcionario.cpf_lineEdit.setText(selectedRow[0].text())
		self.funcionario.nome_lineEdit.setText(selectedRow[1].text())
		self.funcionario.telFixo_lineEdit.setText(selectedRow[2].text())
		self.funcionario.telMovel_lineEdit.setText(selectedRow[3].text())
		self.funcionario.comissao_spinBox.setValue(float(selectedRow[4].text()))
		if self.mainwindow.gerente_radioButton.isChecked():
			self.funcionario.cargo_comboBox.setCurrentIndex(0)
		elif self.mainwindow.garcom_radioButton.isChecked():
			self.funcionario.cargo_comboBox.setCurrentIndex(1)
		else:
			self.funcionario.cargo_comboBox.setCurrentIndex(2)

		funcionario_addDialog.exec_()

	def setupBebida(self):
		bebida_addDialog = QtWidgets.QDialog()
		self.bebida.setupUi(bebida_addDialog)

		self.bebida.buttonBox.rejected.connect(lambda : bebida_addDialog.close())

		return bebida_addDialog

	def on_bebida_addBtn_clicked(self):
		bebida_addDialog = self.setupBebida()

		self.bebida.buttonBox.accepted.connect(lambda : self.save_bebida_and_close(bebida_addDialog))

		bebida_addDialog.exec_()

	def on_bebida_delBtn_clicked(self):
		selectedRow = self.mainwindow.bebida_tableWidget.selectedItems()
		
		self.dbHelper.delete('BEBIDA', ['NOME', 'VOLUME'], [selectedRow[0].text(), selectedRow[1].text()])

		self.searchBebidas()

	def save_bebida_and_close(self, bebida_addDialog):
		nome = self.bebida.nome_lineEdit.text()

		volume = self.bebida.volume_spinBox.value()
		quantidade = self.bebida.quantidade_spinBox.value()
		preco = self.bebida.preco_spinBox.value()

		bandeja = 'S' if self.bebida.bandeja_checkBox.isChecked() else 'N'

		print(self.dbHelper.insertIntoBebida([nome, volume, quantidade, bandeja, preco]))

		self.searchBebidas()

		bebida_addDialog.close()

	def editBebida(self):
		bebida_addDialog = self.setupBebida()

		# TODO edit_bebida_and_close
		self.bebida.buttonBox.accepted.connect(lambda: print('oi'))

		selectedRow = self.mainwindow.bebida_tableWidget.selectedItems()
		self.bebida.nome_lineEdit.setText(selectedRow[0].text())
		self.bebida.volume_spinBox.setValue(int(selectedRow[1].text()))
		self.bebida.quantidade_spinBox.setValue(int(selectedRow[2].text()))

		# TODO bandeja e festa fill

		bebida_addDialog.exec_()

	def setupFornecedor(self):
		fornecedor_addDialog = QtWidgets.QDialog()
		self.fornecedor.setupUi(fornecedor_addDialog)

		for banco in bancos:
			self.fornecedor.banco_comboBox.addItem(banco)

		self.fornecedor.buttonBox.rejected.connect(lambda : fornecedor_addDialog.close())

		return fornecedor_addDialog

	def on_fornecedor_addBtn_clicked(self):
		fornecedor_addDialog = self.setupFornecedor()
		
		self.fornecedor.buttonBox.accepted.connect(lambda : self.save_fornecedor_and_close(fornecedor_addDialog))

		fornecedor_addDialog.exec_()

	def on_fornecedor_delBtn_clicked(self):
		selectedRow = self.mainwindow.fornecedor_tableWidget.selectedItems()
		
		self.dbHelper.delete('FORNECEDOR', ['CNPJ'], [selectedRow[0].text()])

		self.mainwindow.fornecedor_tableWidget.clearContents()
		self.mainwindow.fornecedor_tableWidget.setRowCount(0)

		self.fillFornecedores()

	def save_fornecedor_and_close(self, fornecedor_addDialog):
		nome = self.fornecedor.nome_lineEdit.text()
		cnpj = self.fornecedor.cnpj_lineEdit.text()
		tel = self.fornecedor.tel_lineEdit.text()
		agencia = self.fornecedor.agencia_lineEdit.text()
		conta = self.fornecedor.conta_lineEdit.text()

		banco = bancos[self.fornecedor.banco_comboBox.currentText()]

		if(self.fornecedor.corrente_radioButton.isChecked()):
			tipoConta = 'CC'
		elif(self.fornecedor.poupanca_radioButton.isChecked()):
			tipoConta = 'CP'

		iddados = int(time.time() % 10000000000)
		print(self.dbHelper.insertIntoDadosBancarios([iddados, banco, agencia, conta, tipoConta]))
		print(self.dbHelper.insertIntoFornecedor([cnpj, nome, tel, iddados]))

		self.mainwindow.fornecedor_tableWidget.clearContents()
		self.mainwindow.fornecedor_tableWidget.setRowCount(0)

		self.fillFornecedores()

		fornecedor_addDialog.close()

	def editFornecedor(self):
		fornecedor_addDialog = self.setupFornecedor()
		
		# TODO edit_fornecedor_and_close
		self.fornecedor.buttonBox.accepted.connect(lambda : print('oi'))

		selectedRow = self.mainwindow.fornecedor_tableWidget.selectedItems()
		self.fornecedor.cnpj_lineEdit.setText(selectedRow[0].text())
		self.fornecedor.nome_lineEdit.setText(selectedRow[1].text())
		self.fornecedor.tel_lineEdit.setText(selectedRow[2].text())

		banco = selectedRow[3].text()
		for b in bancos:
			if bancos[b] == banco:
				self.fornecedor.banco_comboBox.setCurrentIndex(self.fornecedor.banco_comboBox.findText(b))
		
		self.fornecedor.agencia_lineEdit.setText(selectedRow[4].text())
		self.fornecedor.conta_lineEdit.setText(selectedRow[5].text())

		conta = selectedRow[6].text()

		if conta == 'CC':
			self.fornecedor.corrente_radioButton.setChecked(True)
		else:
			self.fornecedor.poupanca_radioButton.setChecked(True)

		fornecedor_addDialog.exec_()

	def setupCliente(self):
		cliente_addDialog = QtWidgets.QDialog()
		self.cliente.setupUi(cliente_addDialog)

		for banco in bancos:
			self.cliente.banco_comboBox.addItem(banco)
		for estado in estados:
			self.cliente.estado_comboBox.addItem(estado)

		self.cliente.buttonBox.rejected.connect(lambda : cliente_addDialog.close())

		return cliente_addDialog

	def on_cliente_addBtn_clicked(self):
		cliente_addDialog = self.setupCliente()

		self.cliente.buttonBox.accepted.connect(lambda : self.save_cliente_and_close(cliente_addDialog))

		cliente_addDialog.exec_()

	def on_cliente_delBtn_clicked(self):
		selectedRow = self.mainwindow.cliente_tableWidget.selectedItems()
		
		self.dbHelper.delete('CLIENTE', ['CPF'], [selectedRow[0].text()])

		self.mainwindow.cliente_tableWidget.clearContents()
		self.mainwindow.cliente_tableWidget.setRowCount(0)

		self.fillClientes()

	def save_cliente_and_close(self, cliente_addDialog):
		cpf = self.cliente.cpf_lineEdit.text()
		nome = self.cliente.nome_lineEdit.text()
		telFixo = self.cliente.telFixo_lineEdit.text()
		telMovel = self.cliente.telMovel_lineEdit.text()
		agencia = self.cliente.agencia_lineEdit.text()
		conta = self.cliente.conta_lineEdit.text()
		rua = self.cliente.rua_lineEdit.text()
		numero = self.cliente.n_lineEdit.text()
		cidade = self.cliente.cidade_lineEdit.text()
		cep = self.cliente.cep_lineEdit.text()

		banco = bancos[self.cliente.banco_comboBox.currentText()]
		estado = self.cliente.estado_comboBox.currentText()

		if(self.cliente.corrente_radioButton.isChecked()):
			tipoConta = 'CC'
		elif(self.cliente.poupanca_radioButton.isChecked()):
			tipoConta = 'CP'

		if telFixo == '()-':
			telFixo = None

		iddados = int(time.time() % 10000000000)
		print(self.dbHelper.insertIntoDadosBancarios([iddados, banco, agencia, conta, tipoConta]))
		print(self.dbHelper.insertIntoEndereco([iddados, rua, cidade, estado, numero, cep]))
		print(self.dbHelper.insertIntoCliente([cpf, nome, iddados, telFixo, telMovel, iddados]))

		self.mainwindow.cliente_tableWidget.clearContents()
		self.mainwindow.cliente_tableWidget.setRowCount(0)

		self.fillClientes()

		cliente_addDialog.close()

	def editCliente(self):
		cliente_addDialog = self.setupCliente()

		self.cliente.buttonBox.accepted.connect(lambda : print('oi'))

		selectedRow = self.mainwindow.cliente_tableWidget.selectedItems()
		self.cliente.cnpj_lineEdit.setText(selectedRow[0].text())
		self.cliente.nome_lineEdit.setText(selectedRow[1].text())
		self.cliente.telFixo_lineEdit.setText(selectedRow[2].text())
		self.cliente.telMovel_lineEdit.setText(selectedRow[3].text())

		banco = selectedRow[4].text()
		for b in bancos:
			if bancos[b] == banco:
				self.cliente.banco_comboBox.setCurrentIndex(self.cliente.banco_comboBox.findText(b))

		self.cliente.telMovel_lineEdit.setText(selectedRow[5].text())

		cliente_addDialog.exec_()

	def on_casaDeFesta_addBtn_clicked(self):
		casaDeFesta_addDialog = QtWidgets.QDialog()
		self.casaDeFesta.setupUi(casaDeFesta_addDialog)

		for estado in estados:
			self.casaDeFesta.estado_comboBox.addItem(estado)

		self.casaDeFesta.buttonBox.accepted.connect(lambda : self.save_casaDeFesta_and_close(casaDeFesta_addDialog))
		self.casaDeFesta.buttonBox.rejected.connect(lambda : casaDeFesta_addDialog.close())
		
		casaDeFesta_addDialog.exec_()

	def on_casaDeFesta_delBtn_clicked(self):
		selectedRow = self.mainwindow.casaDeFesta_tableWidget.selectedItems()
		
		self.dbHelper.delete('CASA_FESTA', ['NOME'], [selectedRow[0].text()])

		self.mainwindow.casaDeFesta_tableWidget.clearContents()
		self.mainwindow.casaDeFesta_tableWidget.setRowCount(0)

		self.fillCasasDeFesta()

	def save_casaDeFesta_and_close(self, casaDeFesta_addDialog):
		nome = self.casaDeFesta.nome_lineEdit.text()
		rua = self.casaDeFesta.rua_lineEdit.text()
		numero = self.casaDeFesta.n_lineEdit.text()
		cidade = self.casaDeFesta.cidade_lineEdit.text()
		cep = self.casaDeFesta.cep_lineEdit.text()

		estado = self.casaDeFesta.estado_comboBox.currentText()

		iddados = int(time.time() % 10000000000)
		print(self.dbHelper.insertIntoEndereco([iddados, rua, cidade, estado, numero, cep]))
		print(self.dbHelper.insertIntoCasaFesta([nome, iddados]))

		self.mainwindow.casaDeFesta_comboBox.addItem(nome)

		self.mainwindow.casaDeFesta_tableWidget.clearContents()
		self.mainwindow.casaDeFesta_tableWidget.setRowCount(0)

		self.fillCasasDeFesta()

		casaDeFesta_addDialog.close()

	def on_bebida_addToTableBtn_clicked(self):
		numRows = self.festa.bebidas_tableWidget.rowCount()
		self.festa.bebidas_tableWidget.insertRow(numRows)
		nome = self.festa.bebida_comboBox.currentText() # AQUI PRECISA VER COMO VEM PRA DAR SPLIT
		# NOME -> self.festa.bebidas_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem())
		# VOLUME -> self.festa.bebidas_tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem())
		quantidade = str(self.festa.quantidade_spinBox.value())
		self.festa.bebidas_tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(quantidade))

	def on_garcons_addToTableBtn_clicked(self):
		numRows = self.festa.garcons_tableWidget.rowCount()
		self.festa.garcons_tableWidget.insertRow(numRows)
		nome = self.festa.garcons_comboBox.currentText()
		self.festa.garcons_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(nome))

	def on_operador_addToTableBtn_clicked(self):
		numRows = self.festa.operador_tableWidget.rowCount()
		self.festa.operador_tableWidget.insertRow(numRows)
		nome = self.festa.operador_comboBox.currentText()
		self.festa.operador_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(nome))

	def close(self):
		exit()
		#self.destroy()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	form = MainApp()
	form.showMaximized()
	sys.exit(app.exec_())
