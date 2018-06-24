# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/casadefesta.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(459, 332)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(460, 16777215))
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nome_label = QtWidgets.QLabel(self.frame_2)
        self.nome_label.setObjectName("nome_label")
        self.gridLayout_2.addWidget(self.nome_label, 0, 0, 1, 1)
        self.nome_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.nome_lineEdit.setMaxLength(75)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.gridLayout_2.addWidget(self.nome_lineEdit, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 3)
        self.endereco_label = QtWidgets.QLabel(Dialog)
        self.endereco_label.setObjectName("endereco_label")
        self.gridLayout_3.addWidget(self.endereco_label, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.rua_label = QtWidgets.QLabel(self.frame)
        self.rua_label.setObjectName("rua_label")
        self.gridLayout.addWidget(self.rua_label, 0, 0, 1, 1)
        self.n_label = QtWidgets.QLabel(self.frame)
        self.n_label.setObjectName("n_label")
        self.gridLayout.addWidget(self.n_label, 0, 1, 1, 1)
        self.rua_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.rua_lineEdit.setMaxLength(50)
        self.rua_lineEdit.setObjectName("rua_lineEdit")
        self.gridLayout.addWidget(self.rua_lineEdit, 1, 0, 1, 1)
        self.n_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.n_lineEdit.setMaxLength(5)
        self.n_lineEdit.setObjectName("n_lineEdit")
        self.gridLayout.addWidget(self.n_lineEdit, 1, 1, 1, 2)
        self.cidade_label = QtWidgets.QLabel(self.frame)
        self.cidade_label.setObjectName("cidade_label")
        self.gridLayout.addWidget(self.cidade_label, 2, 0, 1, 1)
        self.estado_label = QtWidgets.QLabel(self.frame)
        self.estado_label.setObjectName("estado_label")
        self.gridLayout.addWidget(self.estado_label, 2, 1, 1, 2)
        self.cidade_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cidade_lineEdit.setMaxLength(20)
        self.cidade_lineEdit.setObjectName("cidade_lineEdit")
        self.gridLayout.addWidget(self.cidade_lineEdit, 3, 0, 1, 1)
        self.estado_comboBox = QtWidgets.QComboBox(self.frame)
        self.estado_comboBox.setObjectName("estado_comboBox")
        self.gridLayout.addWidget(self.estado_comboBox, 3, 1, 1, 2)
        self.cep_label = QtWidgets.QLabel(self.frame)
        self.cep_label.setObjectName("cep_label")
        self.gridLayout.addWidget(self.cep_label, 4, 0, 1, 1)
        self.cep_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cep_lineEdit.setMaxLength(9)
        self.cep_lineEdit.setObjectName("cep_lineEdit")
        self.gridLayout.addWidget(self.cep_lineEdit, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(184, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 3, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Casa de Festa"))
        self.nome_label.setText(_translate("Dialog", "Nome"))
        self.endereco_label.setText(_translate("Dialog", "Endereço"))
        self.rua_label.setText(_translate("Dialog", "Rua"))
        self.n_label.setText(_translate("Dialog", "Nº"))
        self.n_lineEdit.setInputMask(_translate("Dialog", "99999"))
        self.cidade_label.setText(_translate("Dialog", "Cidade"))
        self.estado_label.setText(_translate("Dialog", "Estado"))
        self.cep_label.setText(_translate("Dialog", "CEP"))
        self.cep_lineEdit.setInputMask(_translate("Dialog", "99999-999"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

