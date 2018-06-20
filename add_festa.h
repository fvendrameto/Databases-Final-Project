#ifndef ADD_FESTA_H
#define ADD_FESTA_H

#include <QDialog>

namespace Ui {
class Add_Festa;
}

class Add_Festa : public QDialog
{
    Q_OBJECT

public:
    explicit Add_Festa(QWidget *parent = 0);
    ~Add_Festa();

private:
    Ui::Add_Festa *ui;
};

#endif // ADD_FESTA_H
