# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/bebida.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Bebida(object):
    def setupUi(self, Bebida):
        Bebida.setObjectName("Bebida")
        Bebida.resize(299, 209)
        Bebida.setMinimumSize(QtCore.QSize(0, 0))
        Bebida.setMaximumSize(QtCore.QSize(460, 220))
        Bebida.setBaseSize(QtCore.QSize(240, 440))
        self.gridLayout_2 = QtWidgets.QGridLayout(Bebida)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Bebida)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.nome_label = QtWidgets.QLabel(self.frame)
        self.nome_label.setObjectName("nome_label")
        self.gridLayout.addWidget(self.nome_label, 0, 0, 1, 1)
        self.quantidade_label = QtWidgets.QLabel(self.frame)
        self.quantidade_label.setObjectName("quantidade_label")
        self.gridLayout.addWidget(self.quantidade_label, 0, 2, 1, 1)
        self.nome_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.nome_lineEdit.setMaxLength(30)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.gridLayout.addWidget(self.nome_lineEdit, 1, 0, 1, 2)
        self.quantidade_spinBox = QtWidgets.QSpinBox(self.frame)
        self.quantidade_spinBox.setMaximum(99999)
        self.quantidade_spinBox.setObjectName("quantidade_spinBox")
        self.gridLayout.addWidget(self.quantidade_spinBox, 1, 2, 1, 1)
        self.volume_label = QtWidgets.QLabel(self.frame)
        self.volume_label.setObjectName("volume_label")
        self.gridLayout.addWidget(self.volume_label, 2, 0, 1, 1)
        self.preco_label = QtWidgets.QLabel(self.frame)
        self.preco_label.setObjectName("preco_label")
        self.gridLayout.addWidget(self.preco_label, 2, 2, 2, 1)
        self.volume_spinBox = QtWidgets.QSpinBox(self.frame)
        self.volume_spinBox.setMaximum(99999)
        self.volume_spinBox.setObjectName("volume_spinBox")
        self.gridLayout.addWidget(self.volume_spinBox, 3, 0, 2, 1)
        self.preco_spinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.preco_spinBox.setMaximum(9999.99)
        self.preco_spinBox.setObjectName("preco_spinBox")
        self.gridLayout.addWidget(self.preco_spinBox, 4, 2, 1, 1)
        self.bandeja_checkBox = QtWidgets.QCheckBox(self.frame)
        self.bandeja_checkBox.setObjectName("bandeja_checkBox")
        self.gridLayout.addWidget(self.bandeja_checkBox, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(175, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(112, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Bebida)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(Bebida)
        QtCore.QMetaObject.connectSlotsByName(Bebida)

    def retranslateUi(self, Bebida):
        _translate = QtCore.QCoreApplication.translate
        Bebida.setWindowTitle(_translate("Bebida", "Festa"))
        self.nome_label.setText(_translate("Bebida", "Nome"))
        self.quantidade_label.setText(_translate("Bebida", "Quantidade"))
        self.volume_label.setText(_translate("Bebida", "Volume"))
        self.preco_label.setText(_translate("Bebida", "Preço"))
        self.bandeja_checkBox.setText(_translate("Bebida", "Bandeja"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bebida = QtWidgets.QDialog()
    ui = Ui_Bebida()
    ui.setupUi(Bebida)
    Bebida.show()
    sys.exit(app.exec_())

