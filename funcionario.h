#ifndef FUNCIONARIO_H
#define FUNCIONARIO_H

#include <QDialog>

namespace Ui {
class Funcionario;
}

class Funcionario : public QDialog
{
    Q_OBJECT

public:
    explicit Funcionario(QWidget *parent = 0);
    ~Funcionario();

private slots:
    void on_buttonBox_accepted();

private:
    Ui::Funcionario *ui;
    QString cpf;
    QString nome;
    QString tel_fixo;
    QString tel_mov;
    QString comissao;
    QString cargo;
};

#endif // FUNCIONARIO_H
