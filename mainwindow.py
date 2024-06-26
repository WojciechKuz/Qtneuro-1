import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uistuff.ui_form import Ui_MainWindow #, metrics, votes

# czy profesor ma wszystkie potrzebne pakiety?
# PySide6 (Qt), numpy, matplotlib

# my imports:
import uistuff.uimanager as uim

# this script can be used as program's entry point

# Ten program oparty jest na PySide6, czyli QT dla Pythona.
# Korzystałem z tego już wcześniej ze względu na możliwość zintegrowania z wykresami matplotlib.

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.uiManager = uim.UIManager(self.ui)
        pass

def checklibs():
    pkgs = ['PySide6', 'numpy']
    ihaveall = True
    for p in pkgs:
        try:
            __import__(p)
        except(ImportError):
            print('Nie zainstalowano', p)
            ihaveall = False
    if not ihaveall:
        print('Nalezy je doinstalowac zeby program dzialal, np. za pomoca pip')
        return False
    return True

def startProgram():
    if not checklibs():
        sys.exit(1)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__": # file can be renamed to something nicer and still contain this class
    startProgram()
