"""Quran Reader

This script work as the main script for the Quran reader.
It runs the Quran reader application.

It creates an instance of QApplication class. It then creates an instance
of the QMainWindow class and passes this instance as argument to the setupUi
method of the Ui_MainWindow class. The Ui_MainWindow class is generated by 
the ./bin/pyuic5 script. The setupUi method customizes the QMainWindow 
instance by adding widgets and layouts.

The script then further customizes the QMainWindow instance.

Finally the script runs the applications by calling the exec_ method.
"""

import sys,os

from source.qreader import Ui_MainWindow
from source.qmanager import Ui_Manager
from PyQt5 import QtWidgets

if __name__ == "__main__":    
    app        = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui         = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui_manager = Ui_Manager()
    ui_manager.initialize_ui(ui);
    MainWindow.show()
    sys.exit(app.exec_())
