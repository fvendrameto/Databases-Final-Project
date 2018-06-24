from PyQt5 import QtGui, QtCore, QtWidgets # Import the PyQt5 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import csv
import os
import time

from mainwindow import Ui_MainWindow as MainWindow
from bebida import Ui_Bebida as Bebida
from casadefesta import Ui_Dialog as CasaDeFesta
from cliente import Ui_Dialog as Cliente
from festa import Ui_Add_Festa as Festa
from fornecedor import Ui_Dialog as Fornecedor
from funcionario import Ui_Funcionario as Funcionario
from database.dbHelper import dbHelper

bancos = {
	'Advanced Corretora de Câmbio Ltda. ': '117',
	'Albatross Corretora de Câmbio e Valores S.A ': '172',
	'Ativa Investimentos S.A. Corretora de Títulos Câmbio e Valores': '188',
	'Banco A.J. Renner S.A.': '654',
	'Banco ABC Brasil S.A.': '246',
	'Banco ABN Amro S.A.': '075',
	'Banco Agibank S.A.': '121',
	'Banco Alfa S.A.': '025',
	'Banco Alvorada S.A.': '641',
	'Banco Andbank (Brasil) S.A.': '065',
	'Banco Arbi S.A.': '213',
	'Banco Bandepe S.A.': '024',
	'Banco Barclays S.A.': '740',
	'Banco BM&FBovespa': '096',
	'Banco BMG S.A.': '318',
	'Banco BNP Paribas Brasil S.A.': '752',
	'Banco Boavista Interatlântico S.A.': '248',
	'Banco Bocom BBM S.A. ': '107',
	'Banco Bradescard S.A.': '063',
	'Banco Bradesco BBI S.A.': '036',
	'Banco Bradesco BERJ S.A.': '122',
	'Banco Bradesco Cartões S.A.': '204',
	'Banco Bradesco Financiamentos S.A.': '394',
	'Banco Bradesco S.A.': '237',
	'Banco Brasil Plural S.A. – Banco Múltiplo': '125',
	'Banco Brasileiro de Negócios S.A. – BBN': '081',
	'Banco BS2 S.A.': '218',
	'Banco BTG Pactual S.A.': '208',
	'Banco Caixa Geral – Brasil S.A.': '473',
	'Banco Capital S.A.': '412',
	'Banco Cargill S.A.': '040',
	'Banco Cédula S.A.': '266',
	'Banco Cetelem S.A.': '739',
	'Banco Cifra S.A.': '233',
	'Banco Citibank S.A.': '745',
	'Banco Clássico S.A.': '241',
	'Banco Confidence de Câmbio S.A.': '095',
	'Banco Cooperativo do Brasil S.A. – Bancoob': '756',
	'Banco Cooperativo Sicredi S.A.': '748',
	'Banco Credit Agricole Brasil S.A.': '222',
	'Banco Credit Suisse (Brasil) S.A.': '505',
	'Banco Crefisa S.A.': '069',
	'Banco da Amazônia S.A.': '003',
	'Banco da China Brasil S.A.': '083',
	'Banco Daycoval S.A.': '707',
	'Banco de Brasília S.A. (BRB)': '070',
	'Banco de Crédito e Varejo S.A. – BCV': '250',
	'Banco de Investimento Credit Suisse (Brasil) S.A.': '505',
	'Banco de La Nacion Argentina': '300',
	'Banco de La Provincia de Buenos Aires': '495',
	'Banco de La Republica Oriental del Uruguay': '494',
	'Banco do Brasil S.A.': '001',
	'Banco do Estado de Sergipe S.A.': '047',
	'Banco do Estado do Espírito Santo – Baneste S.A.': '021',
	'Banco do Estado do Pará S.A.': '037',
	'Banco do Estado do Rio Grande do Sul S.A.': '041',
	'Banco do Nordeste do Brasil S.A.': '004',
	'Banco Fator S.A.': '265',
	'Banco Fibra S.A.': '224',
	'Banco Ficsa S.A.': '626',
	'Banco Finaxis S.A.': '094',
	'Banco Guanabara S.A.': '612',
	'Banco Inbursa S.A.': '012',
	'Banco Industrial do Brasil S.A.': '604',
	'Banco Indusval S.A.': '653',
	'Banco Inter S.A.': '077',
	'Banco Intercap S.A.': '630',
	'Banco Internacional do Funchal (Brasil) S.A. – Banif': '719',
	'Banco Investcred Unibanco S.A.': '249',
	'Banco Itaú BBA S.A.': '184',
	'Banco Itaú Consignado S.A.': '029',
	'Banco Itaú Unibanco Holding S.A.': '652',
	'Banco Itaú Unibanco S.A.': '341',
	'Banco ItauBank S.A': '479',
	'Banco J. P. Morgan S.A.': '376',
	'Banco J. Safra S.A.': '074',
	'Banco John Deere S.A.': '217',
	'Banco KDB S.A.': '076',
	'Banco Keb Hana do Brasil S.A.': '757',
	'Banco Luso Brasileiro S.A.': '600',
	'Banco Máxima S.A.': '243',
	'Banco Mercantil do Brasil S.A.': '389',
	'Banco Mizuho do Brasil S.A.': '370',
	'Banco Modal S.A.': '746',
	'Banco Morgan Stanley S.A.': '066',
	'Banco MUFG Brasil S.A.': '456',
	'Banco Nacional de Desenvolvimento Econômico e Social – BNDES': '007',
	'Banco Neon S.A.': '735',
	'Banco Olé Bonsucesso Consignado S.A.': '169',
	'Banco Original do Agronegócio S.A.': '079',
	'Banco Original S.A.': '212',
	'Banco Ourinvest S.A.': '712',
	'Banco Pan S.A.': '623',
	'Banco Paulista S.A.': '611',
	'Banco Pine S.A.': '643',
	'Banco Rabobank International Brasil S.A.': '747',
	'Banco Randon S.A.': '088',
	'Banco Rendimento S.A.': '633',
	'Banco Ribeirão Preto S.A.': '741',
	'Banco Rodobens S.A.': '120',
	'Banco Safra S.A.': '422',
	'Banco Santander (Brasil) S.A.': '033',
	'Banco Semear S.A.': '743',
	'Banco Sistema S.A.': '754',
	'Banco Société Générale Brasil S.A.': '366',
	'Banco Sofisa S.A.': '637',
	'Banco Sumitomo Mitsui Brasileiro S.A.': '464',
	'Banco Topázio S.A.': '082',
	'Banco Triângulo S.A.': '634',
	'Banco Tricury S.A.': '018',
	'Banco Votorantim S.A.': '655',
	'Banco VR S.A.': '610',
	'Banco Western Union do Brasil S.A.': '119',
	'Banco Woori Bank do Brasil S.A.': '124',
	'Bank of America Merrill Lynch Banco Múltiplo S.A.': '755',
	'Barigui Companhia Hipotecária': '268',
	'Bexs Banco de Câmbio S.A. ': '144',
	'Bexs Corretora de Câmbio S.A.': '253',
	'BGC Liquidez Distribuidora de Títulos e Valores Mobiliários Ltda. ': '134',
	'BNY Mellon Banco S.A.': '017',
	'BR Partners Banco de Investimento S.A. ': '126',
	'Brickell (BRK) S.A. Crédito, Financiamento e Investimento': '092',
	'BRL Trust Distribuidora de Títulos e Valores Mobiliários S.A. ': '173',
	'Broker Brasil Corretora de Câmbio Ltda. ': '142',
	'BT Corretora de Câmbio Ltda. ': '080',
	'Caixa Econômica Federal': '104',
	'Caruana S.A. Sociedade de Crédito, Financiamento e Investimento ': '130',
	'Casa do Crédito S.A. Sociedade de Crédito ao Microempreendedor': '159',
	'Central Cooperativa de Crédito no Estado do Espírito Santo – CECOOP': '114',
	'Central de Cooperativas de Economia e Crédito Mútuo do Estado RS – Unicred ': '091',
	'China Construction Bank (Brasil) Banco Múltiplo S.A.': '320',
	'Citibank N.A.': '477',
	'Codepe Corretora de Valores e Câmbio S.A. ': '127',
	'Commerzbank Brasil S.A. – Banco Múltiplo': '163',
	'Confederação Nacional das Cooperativas Centrais Unicred Ltda (Unicred do Brasil)': '136',
	'Confidence Corretora de Câmbio S.A.': '060',
	'Cooperativa Central de Crédito Noroeste Brasileiro Ltda. (CentralCredi)': '097',
	'Cooperativa Central de Crédito Urbano – Cecred': '085',
	'Cooperativa de Crédito Mútuo dos Despachantes de Trânsito de Sta.Catarina e RS': '016',
	'Cooperativa de Crédito Rural da Região da Mogiana': '089',
	'Credicoamo Crédito Rural Cooperativa': '010',
	'Credit Suisse Hedging-Griffo Corretora de Valores S.A.': '011',
	'Cresol – Confederação Nacional Cooperativas Centrais de Crédito e Econ Familiar': '133',
	'Dacasa Financeira S/A – Sociedade de Crédito, Financiamento e Investimento ': '182',
	'Deutsche Bank S.A. – Banco Alemão': '487',
	'Easynvest – Título Corretora de Valores SA ': '140',
	'Facta Financeira S.A. – Crédito Financiamento e Investimento': '149',
	'Fair Corretora de Câmbio S.A. ': '196',
	'Get Money Corretora de Câmbio S.A.': '138',
	'Goldman Sachs do Brasil Banco Múltiplo S.A.': '064',
	'Gradual Corretora de Câmbio, Títulos e Valores Mobiliários S.A. ': '135',
	'Guide Investimentos S.A. Corretora de Valores': '177',
	'Guitta Corretora de Câmbio Ltda. ': '146',
	'Haitong Banco de Investimento do Brasil S.A. ': '078',
	'Hipercard Banco Múltiplo S.A.': '062',
	'HS Financeira S/A Crédito, Financiamento e Investimentos': '189',
	'HSBC Brasil S.A. Banco de Investimento': '269',
	'IB Corretora de Câmbio, Títulos e Valores Mobiliários Ltda. ': '271',
	'ICAP do Brasil Corretora de Títulos e Valores Mobiliários Ltda. ': '157',
	'ICBC do Brasil Banco Múltiplo S.A.': '132',
	'ING Bank N.V.': '492',
	'Intesa Sanpaolo Brasil S.A. – Banco Múltiplo': '139',
	'JPMorgan Chase Bank, National Association': '488',
	'Kirton Bank S.A. (Banco Múltiplo)': '399',
	'Lecca Crédito, Financiamento e Investimento S/A': '105',
	'Levycam – Corretora de Câmbio e Valores Ltda. ': '145',
	'Magliano S.A. Corretora de Cambio e Valores Mobiliarios ': '113',
	'MS Bank S.A. Banco de Câmbio': '128',
	'Multimoney Corretora de Câmbio Ltda': '137',
	'Natixis Brasil S.A. Banco Múltiplo': '014',
	'Nova Futura Corretora de Títulos e Valores Mobiliários Ltda. ': '191',
	'Novo Banco Continental S.A. – Banco Múltiplo': '753',
	'Nu Pagamentos S.A': '260',
	'Oliveira Trust Distribuidora de Títulos e Valores Mobiliários S.A. ': '111',
	'Omni Banco S.A. ': '613',
	'Paraná Banco S.A.': '254',
	'Parmetal Distribuidora de Títulos e Valores Mobiliários Ltda. ': '194',
	'Pernambucanas Financiadora S.A. Crédito, Financiamento e Investimento': '174',
	'Planner Corretora de Valores S.A.': '100',
	'Pólocred Sociedade de Crédito ao Microempreendedor e Empresa de Pequeno Porte': '093',
	'PortoCred S.A. Crédito, Financiamento e Investimento': '108',
	'Renascença Distribuidora de Títulos e Valores Mobiliários Ltda. ': '101',
	'Scotiabank Brasil S.A. Banco Múltiplo': '751',
	'Senso Corretora de Câmbio e Valores Mobiliários S.A. ': '545',
	'Servicoop – Cooperativa de Economia e Crédito Mútuo dos Servidores Públicos Estaduais do Rio': '190',
	'Socred S.A. – Sociedade de Crédito ao Microempreendedor': '183',
	'Standard Chartered Bank (Brasil) S.A. Banco de Investimento': '118',
	'Stone Pagamentos S.A. ': '197',
	'Treviso Corretora de Câmbio S.A. ': '143',
	'Tullett Prebon Brasil Corretora de Valores e Câmbio Ltda. ': '131',
	'UBS Brasil Banco de Investimento S.A.': '129',
	'UBS Brasil Corretora de Câmbio, Títulos e Valores Mobiliários S.A.': '015',
	'Uniprime Central – Central Interestadual de Cooperativas de Crédito Ltda.': '099',
	'Uniprime Norte do Paraná – Cooperativa de Crédito Ltda. ': '084',
	'XP Investimentos Corretora de Câmbio, Títulos e Valores Mobiliários S/A': '102'
}
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

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

		nomeCasasDeFesta = self.dbHelper.getNomeCasasFesta()
		for i, casaDeFesta in enumerate(nomeCasasDeFesta):
			self.mainwindow.casaDeFesta_comboBox.addItem(casaDeFesta[0])

		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.mainwindow.gerente_comboBox.addItem(funcionario[1])

		self.mainwindow.dataInicial_dateEdit.setDate(QtCore.QDate.currentDate())
		self.mainwindow.dataFinal_dateEdit.setDate(QtCore.QDate.currentDate())

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
		self.mainwindow.funcionario_tableWidget.clearContents()
		self.mainwindow.funcionario_tableWidget.setRowCount(0)
		
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
		print(dataInicio)
		allFesta = self.dbHelper.getAllAniversarios(dataInicio, dataFinal, gerente, casaDeFesta)
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

	def on_festa_addBtn_clicked(self):
		festa_addDialog = QtWidgets.QDialog()
		self.festa.setupUi(festa_addDialog)

		nomeCasasDeFesta = self.dbHelper.getNomeCasasFesta()
		for i, casaDeFesta in enumerate(nomeCasasDeFesta):
			self.festa.casaDeFesta_comboBox.addItem(casaDeFesta[0])

		allFuncionario = self.dbHelper.getAllGerentes()
		for i, funcionario in enumerate(allFuncionario):
			self.festa.gerente_comboBox.addItem(funcionario[1])
		
		self.festa.buttonBox.accepted.connect(lambda : self.save_festa_and_close(festa_addDialog))
		self.festa.buttonBox.rejected.connect(lambda : festa_addDialog.close())
		
		self.festa.cliente_pushButton.clicked.connect(self.on_cliente_addBtn_clicked)
		self.festa.casaDeFesta_pushButton.clicked.connect(self.on_casaDeFesta_addBtn_clicked)

		self.festa.bebida_addButton.clicked.connect(self.on_bebida_addToTableBtn_clicked)
		self.festa.garcons_addButton.clicked.connect(self.on_garcons_addToTableBtn_clicked)
		self.festa.operador_addButton.clicked.connect(self.on_operador_addToTableBtn_clicked)

		festa_addDialog.exec_()

	def on_festa_delBtn_clicked(self):
		selectedRow = self.mainwindow.festa_tableWidget.selectedItems()
		
		self.dbHelper.delete('FESTA', ['CLIENTE', 'DATA'], [selectedRow[0].text(), selectedRow[1].text()])

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

		self.dbHelper.insertIntoFesta([cliente, data, convidados, 'A', preco, casaDeFesta, gerente])
		self.dbHelper.insertIntoAniversatio([cliente, data, aniversariante, tema, faixa])

		self.searchFestas()

		festa_addDialog.close()

	def on_funcionario_addBtn_clicked(self):
		funcionario_addDialog = QtWidgets.QDialog()
		self.funcionario.setupUi(funcionario_addDialog)

		self.funcionario.cargo_comboBox.addItem('Gerente')
		self.funcionario.cargo_comboBox.addItem('Garçom')
		self.funcionario.cargo_comboBox.addItem('Operador')

		self.funcionario.buttonBox.accepted.connect(lambda : self.save_funcionario_and_close(funcionario_addDialog))
		self.funcionario.buttonBox.rejected.connect(lambda : funcionario_addDialog.close())

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

		self.dbHelper.insertIntoFuncionario([cpf, nome, telFixo, telMovel, comissao, cargo])

		if cargo == 'Gerente':
			self.mainwindow.gerente_comboBox.addItem(nome)

		self.searchFuncionarios()

		funcionario_addDialog.close()

	def on_bebida_addBtn_clicked(self):
		bebida_addDialog = QtWidgets.QDialog()
		self.bebida.setupUi(bebida_addDialog)

		self.bebida.buttonBox.accepted.connect(lambda : self.save_bebida_and_close(bebida_addDialog))
		self.bebida.buttonBox.rejected.connect(lambda : bebida_addDialog.close())

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

		bandeja = self.bebida.bandeja_checkBox.isChecked()

		self.dbHelper.insertIntoBebida([nome, volume, quantidade, bandeja, preco])

		self.searchBebidas()

		bebida_addDialog.close()

	def on_fornecedor_addBtn_clicked(self):
		fornecedor_addDialog = QtWidgets.QDialog()
		self.fornecedor.setupUi(fornecedor_addDialog)

		for banco in bancos:
			self.fornecedor.banco_comboBox.addItem(banco)

		self.fornecedor.buttonBox.accepted.connect(lambda : self.save_fornecedor_and_close(fornecedor_addDialog))
		self.fornecedor.buttonBox.rejected.connect(lambda : fornecedor_addDialog.close())

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
		self.dbHelper.insertIntoDadosBancarios([iddados, banco, agencia, conta, tipoConta])
		self.dbHelper.insertIntoFornecedor([cnpj, nome, tel, iddados])

		self.mainwindow.fornecedor_tableWidget.clearContents()
		self.mainwindow.fornecedor_tableWidget.setRowCount(0)

		self.fillFornecedores()

		fornecedor_addDialog.close()

	def on_cliente_addBtn_clicked(self):
		cliente_addDialog = QtWidgets.QDialog()
		self.cliente.setupUi(cliente_addDialog)

		for banco in bancos:
			self.cliente.banco_comboBox.addItem(banco)
		for estado in estados:
			self.cliente.estado_comboBox.addItem(estado)

		self.cliente.buttonBox.accepted.connect(lambda : self.save_cliente_and_close(cliente_addDialog))
		self.cliente.buttonBox.rejected.connect(lambda : cliente_addDialog.close())
				
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
		self.dbHelper.insertIntoDadosBancarios([iddados, banco, agencia, conta, tipoConta])
		self.dbHelper.insertIntoEndereco([iddados, rua, cidade, estado, numero, cep])
		self.dbHelper.insertIntoCliente([cpf, nome, iddados, telFixo, telMovel, iddados])

		self.mainwindow.cliente_tableWidget.clearContents()
		self.mainwindow.cliente_tableWidget.setRowCount(0)

		self.fillClientes()

		cliente_addDialog.close()

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
		self.dbHelper.insertIntoEndereco([iddados, rua, cidade, estado, numero, cep])
		self.dbHelper.insertIntoCasaFesta([nome, iddados])

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
