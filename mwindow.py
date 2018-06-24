from PyQt5 import QtGui, QtCore, QtWidgets # Import the PyQt5 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import os
import re
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
from static import bancos, estados, faixasEtaria

def preprocess(string):
	regex = re.compile(r'^([^(]*)\(([^)]*)\)')
	match = regex.match(string)
	return match

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
		self.mainwindow.cliente_tableWidget.cellDoubleClicked.connect(self.editCliente)
		self.mainwindow.casaDeFesta_tableWidget.cellDoubleClicked.connect(self.editCasaDeFesta)

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
				if festa[j] == 'None':
					festa[j] = "Não possui"
				self.mainwindow.festa_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(festa[j]))

	def fillFuncionarioGerentes(self):
		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.funcionario_tableWidget.insertRow(i)
			for j in range(self.mainwindow.funcionario_tableWidget.columnCount()):
				if funcionario[j] == 'None':
					funcionario[j] = "Não possui"
				self.mainwindow.funcionario_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(funcionario[j]))

	def fillFuncionarioGarcons(self):
		allFuncionario = self.dbHelper.getAllGarcons()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.funcionario_tableWidget.insertRow(i)
			for j in range(self.mainwindow.funcionario_tableWidget.columnCount()):
				if funcionario[j] == 'None':
					funcionario[j] = "Não possui"
				self.mainwindow.funcionario_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(funcionario[j]))

	def fillFuncionarioOperadores(self):
		allFuncionario = self.dbHelper.getAllOperadores()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.funcionario_tableWidget.insertRow(i)
			for j in range(self.mainwindow.funcionario_tableWidget.columnCount()):
				if funcionario[j] == 'None':
					funcionario[j] = "Não possui"
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
				if fornecedor[j] == 'None':
					fornecedor[j] = "Não possui"
				self.mainwindow.fornecedor_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(fornecedor[j]))

	def fillClientes(self):
		allCliente = self.dbHelper.getAllClientes()
		for i, cliente in enumerate(allCliente):
			self.mainwindow.cliente_tableWidget.insertRow(i)
			for j in range(self.mainwindow.cliente_tableWidget.columnCount()):
				if cliente[j] == 'None':
					cliente[j] = "Não possui"
				self.mainwindow.cliente_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(cliente[j]))

	def fillCasasDeFesta(self):
		allCasaDeFesta = self.dbHelper.getAllCasasFesta()
		for i, casaDeFesta in enumerate(allCasaDeFesta):
			self.mainwindow.casaDeFesta_tableWidget.insertRow(i)
			for j in range(self.mainwindow.casaDeFesta_tableWidget.columnCount()):
				if casaDeFesta[j] == 'None':
					casaDeFesta[j] = "Não possui"
				self.mainwindow.casaDeFesta_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(casaDeFesta[j]))

	def setupFesta(self):
		festa_addDialog = QtWidgets.QDialog()
		self.festa.setupUi(festa_addDialog)

		self.festa.buttonBox.buttons()[0].setEnabled(False)

		self.festa.data_timeEdit.setDate(QtCore.QDate.currentDate())

		allCliente = self.dbHelper.getAllClientes()
		for i, cliente in enumerate(allCliente):
			self.festa.cliente_comboBox.addItem(f"{cliente[1]} ({cliente[0]})")

		nomeCasasDeFesta = self.dbHelper.getNomeCasasFesta()
		for i, casaDeFesta in enumerate(nomeCasasDeFesta):
			self.festa.casaDeFesta_comboBox.addItem(casaDeFesta[0])

		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.festa.gerente_comboBox.addItem(f"{funcionario[1]} ({funcionario[0]})")

		allFuncionario = self.dbHelper.getGarconsLivres(self.festa.data_timeEdit.date().toPyDate())
		for i, funcionario in enumerate(allFuncionario):
			self.festa.garcons_comboBox.addItem(f"{funcionario[0]} ({funcionario[1]})")

		allFuncionario = self.dbHelper.getOperadoresLivres(self.festa.data_timeEdit.date().toPyDate())
		for i, funcionario in enumerate(allFuncionario):
			self.festa.operador_comboBox.addItem(f"{funcionario[0]} ({funcionario[1]})")

		allBebidas = self.dbHelper.getBebidasInInterval()
		for i, bebida in enumerate(allBebidas):
			self.festa.bebida_comboBox.addItem(f"{bebida[0]} ({bebida[1]}mL)")

		for faixaEtaria in faixasEtaria:
			self.festa.faixa_comboBox.addItem(faixaEtaria)

		for i in range(self.festa.bebidas_tableWidget.columnCount()):
			self.festa.bebidas_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.festa.garcons_tableWidget.columnCount()):
			self.festa.garcons_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		for i in range(self.festa.operador_tableWidget.columnCount()):
			self.festa.operador_tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
		
		self.festa.buttonBox.rejected.connect(lambda : festa_addDialog.close())
		
		self.festa.cliente_pushButton.clicked.connect(self.on_festa_addToClienteBtn_clicked)
		self.festa.casaDeFesta_pushButton.clicked.connect(self.on_festa_addToCasaDeFestaBtn_clicked)
		self.festa.data_timeEdit.dateChanged.connect(self.refreshFuncionariosLivre)
		self.festa.bebida_addButton.clicked.connect(self.on_bebida_addToTableBtn_clicked)
		self.festa.garcons_addButton.clicked.connect(self.on_garcons_addToTableBtn_clicked)
		self.festa.operador_addButton.clicked.connect(self.on_operador_addToTableBtn_clicked)
		self.festa.bebidas_tableWidget.cellDoubleClicked.connect(self.rollbackBebida)
		self.festa.garcons_tableWidget.cellDoubleClicked.connect(self.rollbackGarcom)
		self.festa.operador_tableWidget.cellDoubleClicked.connect(self.rollbackOperador)

		return festa_addDialog

	def on_festa_addBtn_clicked(self):
		festa_addDialog = self.setupFesta()

		self.festa.buttonBox.buttons()[0].setEnabled(True)
		self.festa.buttonBox.accepted.connect(lambda : self.save_festa_and_close(festa_addDialog))

		festa_addDialog.exec_()

	def on_festa_delBtn_clicked(self):
		selectedRow = self.mainwindow.festa_tableWidget.selectedItems()
		
		self.dbHelper.delete('FESTA', ['CLIENTE', 'DATA'], [selectedRow[0].text(), datetime.strptime(selectedRow[1].text(), '%d/%m/%Y')])

		self.dbHelper.commit()
		self.searchFestas()

	def save_festa_and_close(self, festa_addDialog):
		# Data a ser salva:
		data = self.festa.data_timeEdit.date().toPyDate()

		# SpinBox a serem salvos:
		convidados = self.festa.convidados_spinBox.value()
		preco = self.festa.preco_spinBox.value()
		barracas = self.festa.barracas_spinBox.value()

		# Itens de ComboBox a serem salvos:
		faixa = self.festa.faixa_comboBox.currentText()
		cliente = self.festa.cliente_comboBox.currentText()
		if cliente != '':
			cliente = preprocess(cliente)[2]
		casaDeFesta = self.festa.casaDeFesta_comboBox.currentText()
		gerente = self.festa.gerente_comboBox.currentText()
		if gerente != '':
			print(type(gerente))

		# LineEdits a serem salvos:
		aniversariante = self.festa.aniversariante_lineEdit.text()
		tema = self.festa.tema_lineEdit.text()
		
		festa = [cliente, data]
		bebidas = []
		garcons = []
		operadores = []
		for i in range(self.festa.bebidas_tableWidget.rowCount()):
			bebidas.append([self.festa.bebidas_tableWidget.item(i,0).text(), self.festa.bebidas_tableWidget.item(i,1).text(), self.festa.bebidas_tableWidget.item(i,2).text()])

		for i in range(self.festa.garcons_tableWidget.rowCount()):
			garcons.append([self.festa.garcons_tableWidget.item(i,1).text()])

		for i in range(self.festa.operador_tableWidget.rowCount()):
			operadores.append([i, self.festa.operador_tableWidget.item(i,1).text()])

		error = self.checkError(self.dbHelper.insertIntoFesta([cliente, data, convidados, 'A', preco, casaDeFesta, gerente]))
		if not error:
			error = self.checkError(self.dbHelper.insertIntoAniversario([cliente, data, aniversariante, tema, faixa]))
		if not error:
			for bebida in bebidas:
				values = festa + bebida
				error = self.checkError(self.dbHelper.insertIntoBebidaBandejaFesta(values))
		if not error:
			for garcom in garcons:
				values = festa + garcom
				print(values)
				error = self.checkError(self.dbHelper.insertIntoGarcomFesta(values))
		if not error:
			for i, operador in enumerate(operadores):
				values = [(time.time() + i*1000000) % 10000000000]
				values += festa
				values += operador
				error = self.checkError(self.dbHelper.insertIntoBarracaRaspadinha(values))
		if not error:
			self.dbHelper.commit()
			self.searchFestas()
			festa_addDialog.close()
		else:
			self.dbHelper.rollback()

	def editFesta(self):
		festa_addDialog = self.setupFesta()

		self.festa.cliente_comboBox.setEnabled(False)
		self.festa.cliente_pushButton.setEnabled(False)
		self.festa.data_timeEdit.setEnabled(False)

		self.festa.buttonBox.accepted.connect(lambda : self.edit_festa_and_close(festa_addDialog))

		selectedRow = self.mainwindow.festa_tableWidget.selectedItems()

		cliente = self.dbHelper.getCliente(selectedRow[0].text())[0]
		self.festa.cliente_comboBox.setCurrentIndex(self.festa.cliente_comboBox.findText(f'{cliente[1]} ({cliente[0]})'))
		self.festa.data_timeEdit.setDate(datetime.strptime(selectedRow[1].text(), '%d/%m/%Y'))
		self.festa.convidados_spinBox.setValue(int(selectedRow[2].text()))
		self.festa.preco_spinBox.setValue(float(selectedRow[3].text()))

		gerente = self.dbHelper.getGerente(selectedRow[4].text())[0]
		self.festa.gerente_comboBox.setCurrentIndex(self.festa.gerente_comboBox.findText(f'{gerente[1]} ({gerente[0]})'))
		self.festa.casaDeFesta_comboBox.setCurrentIndex(self.festa.casaDeFesta_comboBox.findText(selectedRow[5].text()))
		self.festa.aniversariante_lineEdit.setText(selectedRow[6].text())
		self.festa.tema_lineEdit.setText(selectedRow[7].text())

		self.festa.casaDeFesta_comboBox.currentIndexChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.gerente_comboBox.currentIndexChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.faixa_comboBox.currentIndexChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.convidados_spinBox.valueChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.preco_spinBox.valueChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.casaDeFesta_comboBox.currentIndexChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.gerente_comboBox.currentIndexChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.aniversariante_lineEdit.textChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.tema_lineEdit.textChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.barracas_spinBox.valueChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))
		self.festa.faixa_comboBox.currentIndexChanged.connect(lambda: self.festa.buttonBox.buttons()[0].setEnabled(True))

		festa_addDialog.exec_()

	def edit_festa_and_close(self, festa_addDialog):
		# Data a ser salva:
		data = self.festa.data_timeEdit.dateTime().toPyDate()

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

		error = self.checkError(self.dbHelper.updateFesta([cliente, data], [convidados, 'A', preco, casaDeFesta, gerente]))
		if not error:
			error = self.checkError(self.dbHelper.updateAniversatio([cliente, data], [aniversariante, tema, faixa]))

		if not error:
			self.dbHelper.commit()
			festa_addDialog.close()
		else:
			self.dbHelper.rollback()

	def setupFuncionario(self):
		funcionario_addDialog = QtWidgets.QDialog()
		self.funcionario.setupUi(funcionario_addDialog)

		self.funcionario.buttonBox.buttons()[0].setEnabled(False)

		self.funcionario.cargo_comboBox.addItem('Gerente')
		self.funcionario.cargo_comboBox.addItem('Garçom')
		self.funcionario.cargo_comboBox.addItem('Operador')

		self.funcionario.buttonBox.rejected.connect(lambda : funcionario_addDialog.close())

		return funcionario_addDialog

	def on_funcionario_addBtn_clicked(self):
		funcionario_addDialog = self.setupFuncionario()

		self.funcionario.buttonBox.buttons()[0].setEnabled(True)
		self.funcionario.buttonBox.accepted.connect(lambda : self.save_funcionario_and_close(funcionario_addDialog))

		funcionario_addDialog.exec_()

	def on_funcionario_delBtn_clicked(self):
		selectedRow = self.mainwindow.funcionario_tableWidget.selectedItems()
		
		self.dbHelper.delete('FUNCIONARIO', ['CPF'], [selectedRow[0].text()])
		
		self.dbHelper.commit()
		self.searchFuncionarios()

	def save_funcionario_and_close(self, funcionario_addDialog):
		nome = self.funcionario.nome_lineEdit.text()
		cpf = self.funcionario.cpf_lineEdit.text()
		telFixo = self.funcionario.telFixo_lineEdit.text()
		telMovel = self.funcionario.telMovel_lineEdit.text()

		comissao = self.funcionario.comissao_spinBox.value()

		cargo = self.funcionario.cargo_comboBox.currentText()

		if telFixo == '()-':
			telFixo = None

		error = self.checkError(self.dbHelper.insertIntoFuncionario([cpf, nome, telFixo, telMovel, comissao, cargo]))

		if not error:
			if cargo == 'Gerente':
				self.gerentes[nome] = cpf
				self.mainwindow.gerente_comboBox.addItem(nome)

			self.dbHelper.commit()
			self.searchFuncionarios()
			funcionario_addDialog.close()
		else:
			self.dbHelper.rollback()

	def editFuncionario(self):
		funcionario_addDialog = self.setupFuncionario()

		self.funcionario.cpf_lineEdit.setEnabled(False)

		self.funcionario.buttonBox.accepted.connect(lambda : self.edit_funcionario_and_close(funcionario_addDialog))

		selectedRow = self.mainwindow.funcionario_tableWidget.selectedItems()
		self.funcionario.cpf_lineEdit.setText(selectedRow[0].text())
		self.funcionario.nome_lineEdit.setText(selectedRow[1].text())
		self.funcionario.telMovel_lineEdit.setText(selectedRow[2].text())
		self.funcionario.telFixo_lineEdit.setText(selectedRow[3].text())
		self.funcionario.comissao_spinBox.setValue(float(selectedRow[4].text()))
		if self.mainwindow.gerente_radioButton.isChecked():
			self.funcionario.cargo_comboBox.setCurrentIndex(0)
		elif self.mainwindow.garcom_radioButton.isChecked():
			self.funcionario.cargo_comboBox.setCurrentIndex(1)
		else:
			self.funcionario.cargo_comboBox.setCurrentIndex(2)

		self.funcionario.nome_lineEdit.textChanged.connect(lambda: self.funcionario.buttonBox.buttons()[0].setEnabled(True))
		self.funcionario.telFixo_lineEdit.textChanged.connect(lambda: self.funcionario.buttonBox.buttons()[0].setEnabled(True))
		self.funcionario.telMovel_lineEdit.textChanged.connect(lambda: self.funcionario.buttonBox.buttons()[0].setEnabled(True))
		self.funcionario.comissao_spinBox.valueChanged.connect(lambda: self.funcionario.buttonBox.buttons()[0].setEnabled(True))
		self.funcionario.cargo_comboBox.currentIndexChanged.connect(lambda: self.funcionario.buttonBox.buttons()[0].setEnabled(True))

		funcionario_addDialog.exec_()

	def edit_funcionario_and_close(self, funcionario_addDialog):
		nome = self.funcionario.nome_lineEdit.text()
		cpf = self.funcionario.cpf_lineEdit.text()
		telFixo = self.funcionario.telFixo_lineEdit.text()
		telMovel = self.funcionario.telMovel_lineEdit.text()

		comissao = self.funcionario.comissao_spinBox.value()

		cargo = self.funcionario.cargo_comboBox.currentText()

		if telFixo == '()-':
			telFixo = None

		error = self.checkError(self.dbHelper.updateFuncionario([cpf], [nome, telFixo, telMovel, comissao, cargo]))

		if not error:
			self.dbHelper.commit()
			self.searchFuncionarios()
			funcionario_addDialog.close()
		else:
			self.dbHelper.rollback()

	def setupBebida(self):
		bebida_addDialog = QtWidgets.QDialog()
		self.bebida.setupUi(bebida_addDialog)

		self.bebida.buttonBox.buttons()[0].setEnabled(False)

		self.bebida.buttonBox.rejected.connect(lambda : bebida_addDialog.close())

		return bebida_addDialog

	def on_bebida_addBtn_clicked(self):
		bebida_addDialog = self.setupBebida()

		self.bebida.buttonBox.buttons()[0].setEnabled(True)
		self.bebida.buttonBox.accepted.connect(lambda : self.save_bebida_and_close(bebida_addDialog))

		bebida_addDialog.exec_()

	def on_bebida_delBtn_clicked(self):
		selectedRow = self.mainwindow.bebida_tableWidget.selectedItems()
		
		self.dbHelper.delete('BEBIDA', ['NOME', 'VOLUME'], [selectedRow[0].text(), selectedRow[1].text()])

		self.dbHelper.commit()
		self.searchBebidas()

	def save_bebida_and_close(self, bebida_addDialog):
		nome = self.bebida.nome_lineEdit.text()

		volume = self.bebida.volume_spinBox.value()
		quantidade = self.bebida.quantidade_spinBox.value()
		preco = self.bebida.preco_spinBox.value()

		bandeja = 'S' if self.bebida.bandeja_checkBox.isChecked() else 'N'

		error = self.checkError(self.dbHelper.insertIntoBebida([nome, volume, quantidade, bandeja, preco]))

		if not error:
			self.dbHelper.commit()
			self.searchBebidas()
			bebida_addDialog.close()
		else:
			self.dbHelper.rollback()

	def editBebida(self):
		bebida_addDialog = self.setupBebida()

		self.bebida.nome_lineEdit.setEnabled(False)
		self.bebida.volume_spinBox.setEnabled(False)

		self.bebida.buttonBox.accepted.connect(lambda: self.edit_bebida_and_close(bebida_addDialog))

		selectedRow = self.mainwindow.bebida_tableWidget.selectedItems()
		self.bebida.nome_lineEdit.setText(selectedRow[0].text())
		self.bebida.volume_spinBox.setValue(int(selectedRow[1].text()))
		self.bebida.quantidade_spinBox.setValue(int(selectedRow[2].text()))

		bebida = self.dbHelper.getBebida(self.bebida.nome_lineEdit.text(), str(self.bebida.volume_spinBox.value()))[0]
		self.bebida.preco_spinBox.setValue(float(bebida[2]))

		if bebida[1] == 'S':
			self.bebida.bandeja_checkBox.setChecked(True)

		self.bebida.quantidade_spinBox.valueChanged.connect(lambda: self.bebida.buttonBox.buttons()[0].setEnabled(True))
		self.bebida.preco_spinBox.valueChanged.connect(lambda: self.bebida.buttonBox.buttons()[0].setEnabled(True))
		self.bebida.bandeja_checkBox.clicked.connect(lambda: self.bebida.buttonBox.buttons()[0].setEnabled(True))

		bebida_addDialog.exec_()

	def edit_bebida_and_close(self, bebida_addDialog):
		nome = self.bebida.nome_lineEdit.text()

		volume = self.bebida.volume_spinBox.value()
		quantidade = self.bebida.quantidade_spinBox.value()
		preco = self.bebida.preco_spinBox.value()

		bandeja = 'S' if self.bebida.bandeja_checkBox.isChecked() else 'N'

		error = self.checkError(self.dbHelper.updateBebida([nome, volume], [quantidade, bandeja, preco]))

		if not error:
			self.dbHelper.commit()
			self.searchBebidas()
			bebida_addDialog.close()
		else:
			self.dbHelper.rollback()

	def setupFornecedor(self):
		fornecedor_addDialog = QtWidgets.QDialog()
		self.fornecedor.setupUi(fornecedor_addDialog)

		self.fornecedor.buttonBox.buttons()[0].setEnabled(False)
	
		for banco in bancos:
			self.fornecedor.banco_comboBox.addItem(banco)

		self.fornecedor.buttonBox.rejected.connect(lambda : fornecedor_addDialog.close())

		return fornecedor_addDialog

	def on_fornecedor_addBtn_clicked(self):
		fornecedor_addDialog = self.setupFornecedor()
		
		self.fornecedor.buttonBox.buttons()[0].setEnabled(True)
		self.fornecedor.buttonBox.accepted.connect(lambda : self.save_fornecedor_and_close(fornecedor_addDialog))

		fornecedor_addDialog.exec_()

	def on_fornecedor_delBtn_clicked(self):
		selectedRow = self.mainwindow.fornecedor_tableWidget.selectedItems()
		
		self.dbHelper.delete('FORNECEDOR', ['CNPJ'], [selectedRow[0].text()])

		self.mainwindow.fornecedor_tableWidget.clearContents()
		self.mainwindow.fornecedor_tableWidget.setRowCount(0)

		self.dbHelper.commit()
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
		error = self.checkError(self.dbHelper.insertIntoDadosBancarios([iddados, banco, agencia, conta, tipoConta]))
		if not error:
			error = self.checkError(self.dbHelper.insertIntoFornecedor([cnpj, nome, tel, iddados]))

		if not error:
			self.mainwindow.fornecedor_tableWidget.clearContents()
			self.mainwindow.fornecedor_tableWidget.setRowCount(0)

			self.dbHelper.commit()
			self.fillFornecedores()
			fornecedor_addDialog.close()
		else:
			self.dbHelper.rollback()

	# Configura, preenche e exibe a caixa de diálogo de edição de um Fornecedor
	def editFornecedor(self):
		fornecedor_addDialog = self.setupFornecedor()

		self.fornecedor.cnpj_lineEdit.setEnabled(False)
		
		# Habilita o botão de confirmação como botão para edição
		self.fornecedor.buttonBox.accepted.connect(lambda : self.edit_fornecedor_and_close(fornecedor_addDialog))

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

		# Conecta com os sinais que verificam alterações nos campos
		self.fornecedor.nome_lineEdit.textChanged.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))
		self.fornecedor.tel_lineEdit.textChanged.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))
		self.fornecedor.banco_comboBox.currentIndexChanged.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))
		self.fornecedor.agencia_lineEdit.textChanged.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))
		self.fornecedor.conta_lineEdit.textChanged.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))
		self.fornecedor.corrente_radioButton.clicked.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))
		self.fornecedor.poupanca_radioButton.clicked.connect(lambda: self.fornecedor.buttonBox.buttons()[0].setEnabled(True))

		fornecedor_addDialog.exec_()

	# Armazena os dados durante a edição de um Fornecedor dado e efetua a atualização no banco de dados,
	# caso não haja erros
	def edit_fornecedor_and_close(self, fornecedor_addDialog):
		# Armazena os novos valores
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

		# Armazena o ID dos Dados Bancários do Cliente
		iddados = self.dbHelper.getDadosBancariosFornecedor(cnpj)[0][0]

		# Efetua as atualizações em Dados Bancários e Cliente
		error = self.checkError(self.dbHelper.updateDadosBancarios([iddados], [banco, agencia, conta, tipoConta]))
		if not error:
			error = self.checkError(self.dbHelper.updateFornecedor([cnpj], [nome, tel, iddados]))

		if not error:
			self.mainwindow.fornecedor_tableWidget.clearContents()
			self.mainwindow.fornecedor_tableWidget.setRowCount(0)

			self.dbHelper.commit()
			self.fillFornecedores()
			fornecedor_addDialog.close()
		else:
			self.dbHelper.rollback()

	# Inicializa a caixa de diálogo de Cliente
	def setupCliente(self):
		cliente_addDialog = QtWidgets.QDialog()
		self.cliente.setupUi(cliente_addDialog)

		self.cliente.buttonBox.buttons()[0].setEnabled(False)

		for banco in bancos:
			self.cliente.banco_comboBox.addItem(banco)
		for estado in estados:
			self.cliente.estado_comboBox.addItem(estado)

		# Habilita o botão que cancela a operação na caixa de diálogo
		self.cliente.buttonBox.rejected.connect(lambda : cliente_addDialog.close())

		return cliente_addDialog

	# Abre a caixa de diálogo de adição de um Cliente
	def on_cliente_addBtn_clicked(self):
		cliente_addDialog = self.setupCliente()

		self.cliente.buttonBox.buttons()[0].setEnabled(True)
		self.cliente.buttonBox.accepted.connect(lambda : self.save_cliente_and_close(cliente_addDialog))

		cliente_addDialog.exec_()

	# Remove o Cliente selecionado
	def on_cliente_delBtn_clicked(self):
		selectedRow = self.mainwindow.cliente_tableWidget.selectedItems()
		
		self.dbHelper.delete('CLIENTE', ['CPF'], [selectedRow[0].text()])

		self.mainwindow.cliente_tableWidget.clearContents()
		self.mainwindow.cliente_tableWidget.setRowCount(0)

		self.dbHelper.commit()
		self.fillClientes()
	
	# Salva os dados da caixa de diálogo de adição de um Cliente e, caso não haja erros,
	# insere esta no banco de dados
	def save_cliente_and_close(self, cliente_addDialog):
		# Armazena os valores
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

		# Cria um ID para os Dados Bancários e Endereço do Cliente
		iddados = int(time.time() % 10000000000)
		
		# Insere em Dados Bancários, Endereço e Cliente
		error = self.checkError(self.dbHelper.insertIntoDadosBancarios([iddados, banco, agencia, conta, tipoConta]))
		if not error:
			error = self.checkError(self.dbHelper.insertIntoEndereco([iddados, rua, cidade, estado, numero, cep]))
		if not error:
			error = self.checkError(self.dbHelper.insertIntoCliente([cpf, nome, iddados, telFixo, telMovel, iddados]))

		if not error:
			self.mainwindow.cliente_tableWidget.clearContents()
			self.mainwindow.cliente_tableWidget.setRowCount(0)

			self.dbHelper.commit()
			self.fillClientes()
			cliente_addDialog.close()
		else:
			self.dbHelper.rollback()

	# Configura, preenche e exibe a caixa de diálogo de edição de um Cliente
	def editCliente(self):
		cliente_addDialog = self.setupCliente()

		# Desabilita a edição da chave primária
		self.cliente.cpf_lineEdit.setEnabled(False)

		# Configura o botão de confirmação como botão de edição
		self.cliente.buttonBox.accepted.connect(lambda : self.edit_cliente_and_close(cliente_addDialog))

		# Preenche os campos da caixa de diálogo
		selectedRow = self.mainwindow.cliente_tableWidget.selectedItems()
		self.cliente.cpf_lineEdit.setText(selectedRow[0].text())
		self.cliente.nome_lineEdit.setText(selectedRow[1].text())
		self.cliente.telFixo_lineEdit.setText(selectedRow[2].text())
		self.cliente.telMovel_lineEdit.setText(selectedRow[3].text())

		banco = selectedRow[4].text()
		for b in bancos:
			if bancos[b] == banco:
				self.cliente.banco_comboBox.setCurrentIndex(self.cliente.banco_comboBox.findText(b))

		self.cliente.agencia_lineEdit.setText(selectedRow[5].text())
		self.cliente.conta_lineEdit.setText(selectedRow[6].text())

		conta = selectedRow[7].text()

		if conta == 'CC':
			self.cliente.corrente_radioButton.setChecked(True)
		else:
			self.cliente.poupanca_radioButton.setChecked(True)

		endereco = self.dbHelper.getEnderecoCliente(self.cliente.cpf_lineEdit.text())[0]
		self.cliente.rua_lineEdit.setText(endereco[1])
		self.cliente.n_lineEdit.setText(endereco[2])
		self.cliente.cidade_lineEdit.setText(endereco[3])
		self.cliente.estado_comboBox.setCurrentIndex(self.cliente.estado_comboBox.findText(endereco[4]))
		self.cliente.cep_lineEdit.setText(endereco[5])

		# Conecta com os sinais que verificam alterações nos campos
		self.cliente.nome_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.telFixo_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.telMovel_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.banco_comboBox.currentIndexChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.agencia_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.conta_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.corrente_radioButton.clicked.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.poupanca_radioButton.clicked.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.rua_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.n_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.cidade_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.estado_comboBox.currentIndexChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))
		self.cliente.cep_lineEdit.textChanged.connect(lambda: self.cliente.buttonBox.buttons()[0].setEnabled(True))

		cliente_addDialog.exec_()
	
	# Armazena os dados durante a edição de um Cliente dado e efetua a atualização no banco de dados,
	# caso não haja erros
	def edit_cliente_and_close(self, cliente_addDialog):
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

		# Armazena o ID das tabelas de Endereço e Dados Bancários do Cliente
		id_dadosBancarios = self.dbHelper.getDadosBancariosCliente(cpf)[0][0]
		id_endereco = self.dbHelper.getEnderecoCliente(cpf)[0][0]
		
		# Atualiza as tabelas de Endereço, Dados Bancários e Cliente
		error = self.checkError(self.dbHelper.updateDadosBancarios([id_dadosBancarios], [banco, agencia, conta, tipoConta]))
		if not error:
			error = self.checkError(self.dbHelper.updateEndereco([id_endereco], [rua, cidade, estado, numero, cep]))
		if not error:
			error = self.checkError(self.dbHelper.updateCliente([cpf], [nome, id_dadosBancarios, telFixo, telMovel, id_endereco]))

		if not error:
			self.mainwindow.cliente_tableWidget.clearContents()
			self.mainwindow.cliente_tableWidget.setRowCount(0)

			self.dbHelper.commit()
			self.fillClientes()
			cliente_addDialog.close()
		else:
			self.dbHelper.rollback()

	# Inicializa a caixa de diálogo de Casa de Festa
	def setupCasaDeFesta(self):
		casaDeFesta_addDialog = QtWidgets.QDialog()
		self.casaDeFesta.setupUi(casaDeFesta_addDialog)

		self.casaDeFesta.buttonBox.buttons()[0].setEnabled(False)

		# Adiciona os estados do Brasil na lista de estados do endereço da Casa de Festa
		for estado in estados:
			self.casaDeFesta.estado_comboBox.addItem(estado)

		# Habilita o botão que cancela a operação na caixa de diálogo
		self.casaDeFesta.buttonBox.rejected.connect(lambda : casaDeFesta_addDialog.close())

		return casaDeFesta_addDialog

	# Configura e exibe a caixa de diálogo de adição de uma Casa de Festa
	def on_casaDeFesta_addBtn_clicked(self):
		casaDeFesta_addDialog = self.setupCasaDeFesta()

		# Habilita o botão de confirmação da caixa com botão de adição
		self.casaDeFesta.buttonBox.buttons()[0].setEnabled(True)
		self.casaDeFesta.buttonBox.accepted.connect(lambda : self.save_casaDeFesta_and_close(casaDeFesta_addDialog))
		
		casaDeFesta_addDialog.exec_()

	# Deleta a Casa de festa selecionada
	def on_casaDeFesta_delBtn_clicked(self):
		selectedRow = self.mainwindow.casaDeFesta_tableWidget.selectedItems()
		
		self.dbHelper.delete('CASA_FESTA', ['NOME'], [selectedRow[0].text()])

		self.mainwindow.casaDeFesta_tableWidget.clearContents()
		self.mainwindow.casaDeFesta_tableWidget.setRowCount(0)

		self.dbHelper.commit()
		self.fillCasasDeFesta()

	# Salva os dados da caixa de diálogo de adição de uma Casa de Festa e, caso não haja erros,
	# insere esta no banco de dados
	def save_casaDeFesta_and_close(self, casaDeFesta_addDialog):
		nome = self.casaDeFesta.nome_lineEdit.text()
		rua = self.casaDeFesta.rua_lineEdit.text()
		numero = self.casaDeFesta.n_lineEdit.text()
		cidade = self.casaDeFesta.cidade_lineEdit.text()
		cep = self.casaDeFesta.cep_lineEdit.text()

		estado = self.casaDeFesta.estado_comboBox.currentText()

		# cria um ID para Endereço
		iddados = int(time.time() % 10000000000)

		error = self.checkError(self.dbHelper.insertIntoEndereco([iddados, rua, cidade, estado, numero, cep]))
		if not error:
			error = self.checkError(self.dbHelper.insertIntoCasaFesta([nome, iddados]))

		if not error:
			self.mainwindow.casaDeFesta_comboBox.addItem(nome)
	
			self.mainwindow.casaDeFesta_tableWidget.clearContents()
			self.mainwindow.casaDeFesta_tableWidget.setRowCount(0)

			self.dbHelper.commit()
			self.fillCasasDeFesta()
			casaDeFesta_addDialog.close()
		else:
			self.dbHelper.rollback()

	# Configura, preenche e exibe a caixa de diálogo de edição de uma Casa de Festa
	def editCasaDeFesta(self):
		casaDeFesta_addDialog = self.setupCasaDeFesta()
		
		# Desabilita a edição da chave primária
		self.casaDeFesta.nome_lineEdit.setEnabled(False)

		# Habilita o botão de confirmação da caixa de diálogo como botão de edição
		self.casaDeFesta.buttonBox.accepted.connect(lambda : self.edit_casaDeFesta_and_close(casaDeFesta_addDialog))
		
		# Preenche a caixa de diálogo com os dados da festa dada
		selectedRow = self.mainwindow.casaDeFesta_tableWidget.selectedItems()
		self.casaDeFesta.nome_lineEdit.setText(selectedRow[0].text())
		self.casaDeFesta.rua_lineEdit.setText(selectedRow[1].text())
		self.casaDeFesta.n_lineEdit.setText(selectedRow[2].text())
		self.casaDeFesta.cidade_lineEdit.setText(selectedRow[3].text())
		self.casaDeFesta.cep_lineEdit.setText(selectedRow[4].text())

		endereco = self.dbHelper.getEnderecoCasaFesta(self.casaDeFesta.nome_lineEdit.text())[0]
		self.casaDeFesta.estado_comboBox.setCurrentIndex(self.casaDeFesta.estado_comboBox.findText(endereco[4]))

		# Conecta com os sinais que verificam alterações nos campos
		self.casaDeFesta.rua_lineEdit.textChanged.connect(lambda: self.casaDeFesta.buttonBox.buttons()[0].setEnabled(True))
		self.casaDeFesta.n_lineEdit.textChanged.connect(lambda: self.casaDeFesta.buttonBox.buttons()[0].setEnabled(True))
		self.casaDeFesta.cidade_lineEdit.textChanged.connect(lambda: self.casaDeFesta.buttonBox.buttons()[0].setEnabled(True))
		self.casaDeFesta.estado_comboBox.currentIndexChanged.connect(lambda: self.casaDeFesta.buttonBox.buttons()[0].setEnabled(True))
		self.casaDeFesta.cep_lineEdit.textChanged.connect(lambda: self.casaDeFesta.buttonBox.buttons()[0].setEnabled(True))

		casaDeFesta_addDialog.exec_()

	# Armazena os dados durante a edição de uma Casa de Festa dada e efetua a atualização no banco de dados,
	# caso não haja erros
	def edit_casaDeFesta_and_close(self, casaDeFesta_addDialog):
		nome = self.casaDeFesta.nome_lineEdit.text()
		rua = self.casaDeFesta.rua_lineEdit.text()
		numero = self.casaDeFesta.n_lineEdit.text()
		cidade = self.casaDeFesta.cidade_lineEdit.text()
		cep = self.casaDeFesta.cep_lineEdit.text()

		estado = self.casaDeFesta.estado_comboBox.currentText()

		iddados = self.dbHelper.getEnderecoCasaFesta(nome)[0][0]

		# Atualiza a tabela de Endereços
		error = self.checkError(self.dbHelper.updateEndereco([iddados], [rua, cidade, estado, numero, cep]))
		if not error:
			self.mainwindow.casaDeFesta_tableWidget.clearContents()
			self.mainwindow.casaDeFesta_tableWidget.setRowCount(0)

			self.dbHelper.commit()
			self.fillCasasDeFesta()
			casaDeFesta_addDialog.close()
		else:
			self.dbHelper.rollback()

	# Remove uma Bebidade de uma Festa e retorna ela para a lista de disponíveis para a festa
	def rollbackBebida(self):
		selectedRow = self.festa.bebidas_tableWidget.selectedItems()
		self.festa.bebida_comboBox.addItem(f"{selectedRow[0].text()} ({selectedRow[1].text()}mL)")
		self.festa.bebidas_tableWidget.removeRow(self.festa.bebidas_tableWidget.row(selectedRow[0]))

	# Remove um Garcom de uma Festa e retorna ele para a lista de disponíveis no dia
	def rollbackGarcom(self):
		selectedRow = self.festa.garcons_tableWidget.selectedItems()
		self.festa.garcons_comboBox.addItem(f"{selectedRow[0].text()} ({selectedRow[1].text()}mL)")
		self.festa.garcons_tableWidget.removeRow(self.festa.garcons_tableWidget.row(selectedRow[0]))

	# Remove um Operador de Raspadinha de uma Festa e retorna ele para a lista de disponíveis no dia
	def rollbackOperador(self):
		selectedRow = self.festa.operador_tableWidget.selectedItems()
		self.festa.operador_comboBox.addItem(f"{selectedRow[0].text()} ({selectedRow[1].text()}mL)")
		self.festa.operador_tableWidget.removeRow(self.festa.operador_tableWidget.row(selectedRow[0]))

	# Atualiza a lista de funcionários disponíveis para uma Festa na tela de adição/edição desta
	def refreshFuncionariosLivre(self):
		self.festa.garcons_comboBox.clear()
		self.festa.operador_comboBox.clear()

		allFuncionario = self.dbHelper.getGarconsLivres(self.festa.data_timeEdit.date().toPyDate())
		for i, funcionario in enumerate(allFuncionario):
			self.festa.garcons_comboBox.addItem(f"{funcionario[0]} ({funcionario[1]})")

		allFuncionario = self.dbHelper.getOperadoresLivres(self.festa.data_timeEdit.date().toPyDate())
		for i, funcionario in enumerate(allFuncionario):
			self.festa.operador_comboBox.addItem(f"{funcionario[0]} ({funcionario[1]})")

		self.festa.garcons_tableWidget.clearContents()
		self.festa.operador_tableWidget.clearContents()
		self.festa.garcons_tableWidget.setRowCount(0)
		self.festa.operador_tableWidget.setRowCount(0)

	# Ativa a caixa de diálogo para adição de um Cliente na tela de adição/edição de Festa
	def on_festa_addToClienteBtn_clicked(self):
		self.on_cliente_addBtn_clicked()
		
		self.festa.cliente_comboBox.clear()
		allCliente = self.dbHelper.getAllClientes()
		for i, cliente in enumerate(allCliente):
			self.festa.cliente_comboBox.addItem(f"{cliente[1]} ({cliente[0]})")

	# Ativa a caixa de diálogo para adição de uma Casa de Festa na tela de adição/edição de Festa
	def on_festa_addToCasaDeFestaBtn_clicked(self):
		self.on_casaDeFesta_addBtn_clicked()

		self.festa.casaDeFesta_comboBox.clear()
		nomeCasasDeFesta = self.dbHelper.getNomeCasasFesta()
		for i, casaDeFesta in enumerate(nomeCasasDeFesta):
			self.festa.casaDeFesta_comboBox.addItem(casaDeFesta[0])

	# Adiciona a Bebida escolhida e a quantidade da mesma a uma Festa, durante adição/edição desta
	def on_bebida_addToTableBtn_clicked(self):
		self.festa.buttonBox.buttons()[0].setEnabled(True)
		nome = self.festa.bebida_comboBox.currentText()

		if nome != '':
			self.festa.bebida_comboBox.removeItem(self.festa.bebida_comboBox.currentIndex())
	
			regex = re.compile(r'^([^(]*)\(([^m]*)mL\)')
			match = regex.match(nome)
	
			quantidade = str(self.festa.quantidade_spinBox.value())
	
			numRows = self.festa.bebidas_tableWidget.rowCount()
			self.festa.bebidas_tableWidget.insertRow(numRows)
			self.festa.bebidas_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(match[1][:-1]))
			self.festa.bebidas_tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(match[2]))
			self.festa.bebidas_tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(quantidade))

	# Adiciona o Garçom escolhido a uma Festa, durante adição/edição desta
	def on_garcons_addToTableBtn_clicked(self):
		self.festa.buttonBox.buttons()[0].setEnabled(True)
		nome = self.festa.garcons_comboBox.currentText()

		if nome != '':
			self.festa.garcons_comboBox.removeItem(self.festa.garcons_comboBox.currentIndex())
	
			match = preprocess(nome)
	
			numRows = self.festa.garcons_tableWidget.rowCount()
			self.festa.garcons_tableWidget.insertRow(numRows)
			self.festa.garcons_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(match[1][:-1]))
			self.festa.garcons_tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(match[2]))

	# Adiciona o Operador de Raspadinha escolhido a uma Festa, durante a adição/edição desta
	def on_operador_addToTableBtn_clicked(self):
		self.festa.buttonBox.buttons()[0].setEnabled(True)
		nome = self.festa.operador_comboBox.currentText()
		
		if nome != '' and self.festa.barracas_spinBox.value() > self.festa.operador_tableWidget.rowCount():
			self.festa.operador_comboBox.removeItem(self.festa.operador_comboBox.currentIndex())
	
			match = preprocess(nome)
	
			numRows = self.festa.operador_tableWidget.rowCount()
			self.festa.operador_tableWidget.insertRow(numRows)
			self.festa.operador_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(match[1][:-1]))
			self.festa.operador_tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(match[2]))

	# Confere se há um erro e exibe a caixa de diálogo desse erro, caso exista
	def checkError(self, error):
		if error is not None:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText(error)
			msg.setWindowTitle("Error")
			msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)
			msg.exec_()

			return True
		else:
			return False

	# Encerra a execução do programa
	def close(self):
		exit()

# Enicializa a interface quando o programa é executado a partir desse arquivo
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	form = MainApp()
	form.showMaximized()
	sys.exit(app.exec_())
