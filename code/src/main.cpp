#include <QtWidgets>
#include "addressbook.h"

//! [main function]
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    AddressBook addressBook;
    addressBook.show();

    return app.exec();
}
//! [main function]