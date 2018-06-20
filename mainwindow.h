#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "add_festa.h"
#include "funcionario.h"
#include "bebida.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_3_clicked();

    void on_add_funcionario_clicked();

    void on_add_festa_clicked();

    void on_add_bebida_clicked();

private:
    Ui::MainWindow *ui;
    Add_Festa *festa;
    Funcionario *funcionario;
    Bebida *bebida;
};

#endif // MAINWINDOW_H
