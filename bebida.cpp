#include "bebida.h"
#include "ui_bebida.h"

Bebida::Bebida(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Bebida)
{
    ui->setupUi(this);
}

Bebida::~Bebida()
{
    delete ui;
    nome = ui->nome->text();
    volume = ui->volume->value();
    quantidade = ui->quantidade->value();
    preco = ui->preco->value();
    bandeja = ui->bandeja->checkState();
}
