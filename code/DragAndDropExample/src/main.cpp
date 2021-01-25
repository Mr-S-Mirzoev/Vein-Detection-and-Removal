#include <QApplication>

#include "dragwidget.h"

int main(int argc, char *argv[])
{
    Q_INIT_RESOURCE(fridge);

    QApplication app(argc, argv);
#ifdef QT_KEYPAD_NAVIGATION
    QApplication::setNavigationMode(Qt::NavigationModeCursorAuto);
#endif
    DragWidget window;

    bool smallScreen = QApplication::arguments().contains(QStringLiteral("-small-screen"));
    if (smallScreen)
        window.showFullScreen();
    else
        window.show();

    return app.exec();
}