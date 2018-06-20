#include "funcionario.h"
#include "ui_funcionario.h"
#include <QMessageBox>

Funcionario::Funcionario(QWidget *parent) : QDialog(parent),ui(new Ui::Funcionario) {
    ui->setupUi(this);
    QStringList list=(QStringList()<<"Gerente"<<"Garçom"<<"Bartender"<<"Operador Raspadinha");
    ui->cargo->addItems(list);
}

Funcionario::~Funcionario()
{
    delete ui;
}

void Funcionario::on_buttonBox_accepted()
{
    cpf = ui->cpf->text();
    nome = ui->nome->text();
    tel_fixo = ui->tel_fixo->text();
    tel_mov = ui->tel_mov->text();
    comissao = ui->comissao->text();
    cargo = ui->cargo->currentText();
}
