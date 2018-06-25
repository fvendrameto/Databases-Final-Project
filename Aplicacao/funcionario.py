# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Funcionario(object):
    def setupUi(self, Funcionario):
        Funcionario.setObjectName("Funcionario")
        Funcionario.resize(372, 232)
        Funcionario.setMinimumSize(QtCore.QSize(0, 0))
        Funcionario.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Funcionario.setBaseSize(QtCore.QSize(240, 440))
        self.gridLayout_2 = QtWidgets.QGridLayout(Funcionario)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Funcionario)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.nome_label = QtWidgets.QLabel(self.frame)
        self.nome_label.setObjectName("nome_label")
        self.gridLayout.addWidget(self.nome_label, 0, 0, 1, 1)
        self.telFixo_label = QtWidgets.QLabel(self.frame)
        self.telFixo_label.setObjectName("telFixo_label")
        self.gridLayout.addWidget(self.telFixo_label, 0, 1, 1, 1)
        self.nome_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.nome_lineEdit.setMaxLength(75)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.gridLayout.addWidget(self.nome_lineEdit, 1, 0, 1, 1)
        self.telFixo_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.telFixo_lineEdit.setMaxLength(13)
        self.telFixo_lineEdit.setPlaceholderText("")
        self.telFixo_lineEdit.setObjectName("telFixo_lineEdit")
        self.gridLayout.addWidget(self.telFixo_lineEdit, 1, 1, 1, 1)
        self.cpf_label = QtWidgets.QLabel(self.frame)
        self.cpf_label.setObjectName("cpf_label")
        self.gridLayout.addWidget(self.cpf_label, 2, 0, 1, 1)
        self.telMovel_label = QtWidgets.QLabel(self.frame)
        self.telMovel_label.setObjectName("telMovel_label")
        self.gridLayout.addWidget(self.telMovel_label, 2, 1, 1, 1)
        self.cpf_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cpf_lineEdit.setMaxLength(14)
        self.cpf_lineEdit.setPlaceholderText("")
        self.cpf_lineEdit.setObjectName("cpf_lineEdit")
        self.gridLayout.addWidget(self.cpf_lineEdit, 3, 0, 1, 1)
        self.telMovel_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.telMovel_lineEdit.setMaxLength(14)
        self.telMovel_lineEdit.setPlaceholderText("")
        self.telMovel_lineEdit.setObjectName("telMovel_lineEdit")
        self.gridLayout.addWidget(self.telMovel_lineEdit, 3, 1, 1, 1)
        self.comissao_label = QtWidgets.QLabel(self.frame)
        self.comissao_label.setObjectName("comissao_label")
        self.gridLayout.addWidget(self.comissao_label, 4, 0, 1, 1)
        self.cargo_label = QtWidgets.QLabel(self.frame)
        self.cargo_label.setObjectName("cargo_label")
        self.gridLayout.addWidget(self.cargo_label, 4, 1, 1, 1)
        self.comissao_spinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.comissao_spinBox.setMaximum(99999.99)
        self.comissao_spinBox.setObjectName("comissao_spinBox")
        self.gridLayout.addWidget(self.comissao_spinBox, 5, 0, 1, 1)
        self.cargo_comboBox = QtWidgets.QComboBox(self.frame)
        self.cargo_comboBox.setObjectName("cargo_comboBox")
        self.gridLayout.addWidget(self.cargo_comboBox, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Funcionario)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(Funcionario)
        QtCore.QMetaObject.connectSlotsByName(Funcionario)

    def retranslateUi(self, Funcionario):
        _translate = QtCore.QCoreApplication.translate
        Funcionario.setWindowTitle(_translate("Funcionario", "Funcionario"))
        self.nome_label.setText(_translate("Funcionario", "Nome"))
        self.telFixo_label.setText(_translate("Funcionario", "Telefone Fixo"))
        self.telFixo_lineEdit.setInputMask(_translate("Funcionario", "(99)9999-9999"))
        self.cpf_label.setText(_translate("Funcionario", "CPF"))
        self.telMovel_label.setText(_translate("Funcionario", "Telefone Móvel"))
        self.cpf_lineEdit.setInputMask(_translate("Funcionario", "999.999.999-99"))
        self.telMovel_lineEdit.setInputMask(_translate("Funcionario", "(99)99999-9999"))
        self.comissao_label.setText(_translate("Funcionario", "Comissão"))
        self.cargo_label.setText(_translate("Funcionario", "Cargo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Funcionario = QtWidgets.QDialog()
    ui = Ui_Funcionario()
    ui.setupUi(Funcionario)
    Funcionario.show()
    sys.exit(app.exec_())

