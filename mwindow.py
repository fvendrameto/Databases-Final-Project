from PyQt5 import QtGui, QtCore, QtWidgets # Import the PyQt5 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import csv
import os

from mainwindow import Ui_MainWindow as MainWindow
from bebida import Ui_Bebida as Bebida
from casadefesta import Ui_Dialog as CasaDeFesta
from cliente import Ui_Dialog as Cliente
from festa import Ui_Add_Festa as Festa
from fornecedor import Ui_Dialog as Fornecedor
from funcionario import Ui_Funcionario as Funcionario



class MainApp(QtWidgets.QMainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.mainwindow = MainWindow()
		self.mainwindow.setupUi(self)
		
		self.bebida = Bebida()
		self.casaDeFesta = CasaDeFesta()
		self.cliente = Cliente()
		self.festa = Festa()
		self.fornecedor = Fornecedor()
		self.funcionario = Funcionario()

		self.mainwindow.festa_addButton.clicked.connect(self.on_festa_addBtn_clicked)
		self.mainwindow.festa_delButton.clicked.connect(self.on_festa_delBtn_clicked)

	def on_festa_addBtn_clicked(self):
		festa_addDialog = QtWidgets.QDialog()
		self.festa.setupUi(festa_addDialog)
		self.festa.buttonBox.accepted.connect(lambda : self.save_festa_and_close(festa_addDialog))
		self.festa.buttonBox.rejected.connect(lambda : festa_addDialog.close())
		
		self.festa.cliente_pushButton.clicked.connect(self.on_cliente_addBtn_clicked)
		self.festa.casaDeFesta_pushButton.clicked.connect(self.on_casaDeFesta_addBtn_clicked)
		self.festa.gerente_pushButton.clicked.connect(self.on_gerente_addBtn_clicked)

		self.festa.bebida_addButton.connect(self.on_bebida_addToTableBtn_clicked)
		self.festa.garcons_addButton.connect(self.on_bebida_addToTableBtn_clicked)
		self.festa.operador_addButton.connect(self.on_bebida_addToTableBtn_clicked)

		festa_addDialog.exec_()

	def save_festa_and_close(self, festa_addDialog):
		# Data a ser salva:
		data = self.festa.data_timeEdit.dateTime().toString()

		# SpinBox a serem salvos:
		convidados = self.festa.convidados_spinBox.value()
		preco = self.festa.preco_spinBox.value()
		barracas = self.festa.barracas_spinBox.value()

		# Itens de ComboBox a serem salvos:
		faixa = self.festa.faixa_comboBox.itemText()
		cliente = self.festa.cliente_comboBox.itemText()
		casaDeFesta = self.festa.casaDeFesta_comboBox.itemText()
		gerente = self.festa.gerente_comboBox.itemText()

		# LineEdits a serem salvos:
		festa = self.festa.aniversariante_lineEdit.text()
		tema = self.festa.tema_lineEdit.text()

		festa_addDialog.close()

	def on_cliente_addBtn_clicked(self):
		cliente_addDialog = QtWidgets.QDialog()
		self.cliente.setupUi(cliente_addDialog)

		self.cliente.buttonBox.accepted.connect(lambda : self.save_cliente_and_close(cliente_addDialog))
		self.cliente.buttonBox.rejected.connect(lambda : cliente_addDialog.close())
				
		cliente_addDialog.exec_()

	def save_cliente_and_close(cliente_addDialog):
		cpf = self.cliente.cpf_lineEdit.text()
		nome = self.cliente.nome_lineEdit.text()
		telFixo = self.cliente.telFixo_lineEdit.text()
		telMovel = self.cliente.telMovel_lineEdit.text()
		agencia = self.cliente.agencia_lineEdit.text()
		conta = self.cliente.conta_lineEdit.text()
		rua = self.cliente.rua_lineEdit.text()
		numero = self.cliente.numero_lineEdit.text()
		cidade = self.cliente.cidade_lineEdit.text()
		cep = self.cliente.cep_lineEdit.text()

		banco = self.cliente.banco_comboBox.itemText()
		estado = self.cliente.estado_comboBox.itemText()

		if(self.cliente.corrente_radioButton.isChecked()):
			tipoConta = 'CC'
		elif(self.cliente.poupanca_radioButton.isChecked()):
			tipoConta = 'CP'

		cliente_addDialog.close()

	def on_casaDeFesta_addBtn_clicked(self):
		casaDeFesta_addDialog = QtWidgets.QDialog()
		self.casaDeFesta.setupUi(casaDeFesta_addDialog)

		self.casaDeFesta.buttonBox.accepted.connect(lambda : self.save_casaDeFesta_and_close(casaDeFesta_addDialog))
		self.casaDeFesta.buttonBox.rejected.connect(lambda : casaDeFesta_addDialog.close())
		
		casaDeFesta_addDialog.exec_()

	def save_casaDeFesta_and_close(self, casaDeFesta_addDialog):
		nome = self.casaDeFesta.nome_lineEdit.text()
		rua = self.casaDeFesta.rua_lineEdit.text()
		numero = self.casaDeFesta.numero_lineEdit.text()
		cidade = self.casaDeFesta.cidade_lineEdit.text()
		cep = self.casaDeFesta.cep_lineEdit.text()

		estado = self.casaDeFesta.estado_comboBox.itemText()

	def on_bebida_addToTableBtn_clicked(self):
		numRows = self.festa.bebidas_tableWidget.rowCount()
		self.festa.bebidas_tableWidget.insertRow(numRows)
		# self.festa.bebidas_tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem())
		# self.festa.bebidas_tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem())
		self.festa.bebidas_tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem())


	def close(self):
		exit()
		#self.destroy()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	form = MainApp()
	form.show()
	sys.exit(app.exec_())
