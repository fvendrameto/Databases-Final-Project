#ifndef BEBIDA_H
#define BEBIDA_H

#include <QDialog>

namespace Ui {
class Bebida;
}

class Bebida : public QDialog
{
    Q_OBJECT

public:
    explicit Bebida(QWidget *parent = 0);
    ~Bebida();

private:
    Ui::Bebida *ui;
    QString nome;
    int volume;
    int quantidade;
    double preco;
    bool bandeja;
};

#endif // BEBIDA_H
