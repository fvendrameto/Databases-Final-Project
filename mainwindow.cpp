#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent):QMainWindow(parent),ui(new Ui::MainWindow) {
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}


void MainWindow::on_add_festa_clicked() {
    festa = new Add_Festa(this);
    festa->show();
}

void MainWindow::on_add_funcionario_clicked() {
    funcionario = new Funcionario(this);
    funcionario->show();
}

void MainWindow::on_add_bebida_clicked() {
    bebida = new Bebida(this);
    bebida->show();
}
