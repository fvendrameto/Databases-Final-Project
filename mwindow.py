from PyQt5 import QtGui, QtCore, QtWidgets # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import csv
import os

import mainwindow


from bebida import Ui_Bebida as Bebida
from casadefesta import Ui_Dialog as CasaDeFesta
from cliente import Ui_Dialog as Cliente
from festa import Ui_Add_Festa as Festa
from fornecedor import Ui_Dialog as Fornecedor
from funcionario import Ui_Funcionario as Funcionario



class MainApp(QtWidgets.QMainWindow):
	def __init__(self):
		# Explaining super is out of the scope of this article
		# So please google it if you're not familar with it
		# Simple reason why we use it here is that it allows us to
		# access variables, methods etc in the design.py file
		super(self.__class__, self).__init__()
		self.ui = mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.festa_addButton.clicked.connect(self.on_festa_add_clicked)
		self.ui.festa_delButton.clicked.connect(self.on_festa_del_clicked)
		self.ui.tabWidget.addTab(self.ui.festa, "")


	def on_festa_add_clicked(self):
		festa_add = QtWidgets.QDialog()
		ui = Festa()
		ui.setupUi(festa_add)
		festa_add.exec_()
	def on_festa_del_clicked(self):
		pass
		# bebida_del = QtWidgets.QDialog()
		# ui = Ui_Bebida()
		# ui.setupUi(bebida_del)
		# widget.exec_()



	def close(self):
		exit()
		#self.destroy()


if __name__ == '__main__':              # if we're running file directly and not importing it
	app = QtWidgets.QApplication(sys.argv)
	form = MainApp()
	form.show()
	sys.exit(app.exec_())
