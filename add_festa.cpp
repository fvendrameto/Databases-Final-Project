#include "add_festa.h"
#include "ui_add_festa.h"

Add_Festa::Add_Festa(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Add_Festa)
{
    ui->setupUi(this);
}

Add_Festa::~Add_Festa()
{
    delete ui;
}
