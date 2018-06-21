# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bebida.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Bebida(object):
    def setupUi(self, Bebida):
        Bebida.setObjectName("Bebida")
        Bebida.resize(460, 220)
        Bebida.setMinimumSize(QtCore.QSize(0, 0))
        Bebida.setMaximumSize(QtCore.QSize(460, 220))
        Bebida.setBaseSize(QtCore.QSize(240, 440))
        self.nome_label = QtWidgets.QLabel(Bebida)
        self.nome_label.setGeometry(QtCore.QRect(20, 20, 58, 16))
        self.nome_label.setObjectName("nome_label")
        self.nome_lineEdit = QtWidgets.QLineEdit(Bebida)
        self.nome_lineEdit.setGeometry(QtCore.QRect(20, 40, 201, 28))
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.volume_label = QtWidgets.QLabel(Bebida)
        self.volume_label.setGeometry(QtCore.QRect(20, 80, 58, 16))
        self.volume_label.setObjectName("volume_label")
        self.volume_spinBox = QtWidgets.QSpinBox(Bebida)
        self.volume_spinBox.setGeometry(QtCore.QRect(20, 100, 201, 28))
        self.volume_spinBox.setMaximum(9999)
        self.volume_spinBox.setObjectName("volume_spinBox")
        self.quantidade_label = QtWidgets.QLabel(Bebida)
        self.quantidade_label.setGeometry(QtCore.QRect(240, 20, 81, 16))
        self.quantidade_label.setObjectName("quantidade_label")
        self.quantidade_spinBox = QtWidgets.QSpinBox(Bebida)
        self.quantidade_spinBox.setGeometry(QtCore.QRect(240, 40, 201, 28))
        self.quantidade_spinBox.setObjectName("quantidade_spinBox")
        self.bandeja_checkBox = QtWidgets.QCheckBox(Bebida)
        self.bandeja_checkBox.setGeometry(QtCore.QRect(20, 140, 71, 28))
        self.bandeja_checkBox.setObjectName("bandeja_checkBox")
        self.preco_spinBox = QtWidgets.QDoubleSpinBox(Bebida)
        self.preco_spinBox.setGeometry(QtCore.QRect(240, 100, 201, 28))
        self.preco_spinBox.setObjectName("preco_spinBox")
        self.preco_label = QtWidgets.QLabel(Bebida)
        self.preco_label.setGeometry(QtCore.QRect(240, 80, 81, 16))
        self.preco_label.setObjectName("preco_label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Bebida)
        self.buttonBox.setGeometry(QtCore.QRect(135, 170, 190, 34))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Bebida)
        QtCore.QMetaObject.connectSlotsByName(Bebida)

    def retranslateUi(self, Bebida):
        _translate = QtCore.QCoreApplication.translate
        Bebida.setWindowTitle(_translate("Bebida", "Dialog"))
        self.nome_label.setText(_translate("Bebida", "Nome"))
        self.volume_label.setText(_translate("Bebida", "Volume"))
        self.quantidade_label.setText(_translate("Bebida", "Quantidade"))
        self.bandeja_checkBox.setText(_translate("Bebida", "Bandeja"))
        self.preco_label.setText(_translate("Bebida", "Preço"))

