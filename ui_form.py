# -*- coding: utf-8 -*-

# Do not run this file, it's library for another python script

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QCheckBox,
    QPushButton, QSpinBox, QVBoxLayout, QTableWidget, QTableWidgetItem, QLCDNumber)

from mytableview import MyTableView

colours = {
	0: "blue",
	1: "cyan",
	2: "#0f0",
	3: "orange",
	4: "red",
	5: "magenta",
	229: "#229"
}

class Ui_MainWindow(object):
    # Width and height of window. Window can be scaled, but this values are default.
    window_w = 640
    window_h = 480
    window_name = u"QTe Cyfry 🐍" # u for unicode string
    table_columns = 5
    table_rows = 7
    table_colSize = 50
    table_rowSize = 50

    # Get graph via: UI_MainWindowInstance.graph

    def setupUi(self, MainWindow):
        # main window
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(self.window_w, self.window_h)
        # central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # menu bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        # status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.__populateHLayout()
        self.__populateTableLayout()
        self.__populateVLayout()

        self.retranslateUi(MainWindow) # who cares ???

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def __populateHLayout(self):
        # h layout
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        #self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # add graph layout to h layout
        self.tableLayout = QVBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.horizontalLayout.addLayout(self.tableLayout, stretch=6)
        
        # add v layout to h layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout, stretch=2)

        pass

    def __populateTableLayout(self):
        
        # add graph layout to h layout
        self.tableWidget = MyTableView()
        self.tableWidget.setObjectName(u"tableLayout")
        self.tableLayout.addWidget(self.tableWidget, stretch=6)

        self.tableWidget.setRowCount(self.table_rows)
        self.tableWidget.setColumnCount(self.table_columns)

        for i in range(self.table_columns):
            self.tableWidget.setColumnWidth(i, self.table_colSize)
        for i in range(self.table_rows):
            self.tableWidget.setRowHeight(i, self.table_rowSize)
        for x in range(self.tableWidget.columnCount()):
            for y in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(y, x, QTableWidgetItem(""))

        # Hide row and column headers
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        pass

    def connectHandleSelectionChanged(self, recieverFun):
        self.tableWidget.itemSelectionChanged.connect(recieverFun)
        pass
    def setMouseReleaseReciever(self, recieverFun):
        self.tableWidget.setMyMouseReleaseReciever(recieverFun)
        pass

    def __populateVLayout(self):
        labelPolicy = QSizePolicy()
        labelPolicy.verticalPolicy = QSizePolicy.Policy.Minimum

        # lcd number
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.display(".")
        self.verticalLayout.addWidget(self.lcdNumber)
        
        # lcd label
        self.lcdLabel = QLabel(self.centralwidget)
        self.lcdLabel.setObjectName(u"lcdLabel")
        self.lcdLabel.setText(u"Tu wyświetlą się wykryte cyfry ⬆\nJeśli nic nie wykryto, wyświetli kropkę")
        self.lcdLabel.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.lcdLabel)

        # detect digit button
        self.detectButt = QPushButton()
        self.detectButt.setObjectName(u"detectButton")
        self.detectButt.setText(u"wykryj cyfrę") # &a means a is used as shortcut key
        self.detectButt.setShortcut("d")
        #self.detectButt.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.detectButt)

        # auto detect selection box (default true)
        self.detectCheckbox = QCheckBox(self.centralwidget)
        self.detectCheckbox.setObjectName(u"detectCheckbox")
        self.detectCheckbox.setText(u"&Automatyczne wykrywanie cyfr")
        self.detectCheckbox.setChecked(True)
        #self.detectCheckbox.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.detectCheckbox)

        # copy digit text field
        self.digitText = QLabel(self.centralwidget)
        self.digitText.setObjectName(u"resizeText")
        self.digitText.setText(u"\nTu będzie cyfra do skopiowania\n")
        self.digitText.setSizePolicy(labelPolicy)
        self.digitText.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.verticalLayout.addWidget(self.digitText)

        # clean grid button
        self.cleanButt = QPushButton()
        self.cleanButt.setObjectName(u"cleanButton")
        self.cleanButt.setText(u"wy&czyść pole") # &a means a is used as shortcut key
        #self.detectCheckbox.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.cleanButt)

        # widget for spacing
        self.spaceWidget = QWidget(self.centralwidget)
        self.spaceWidget.setObjectName(u"spaceWidget")
        self.verticalLayout.addWidget(self.spaceWidget)

        # hint text
        hint1 = u"ℹ\nAby zobaczyć, co znajduje się pod\nzaznaczonym opszarem,\nodkliknij poza tabelą."
        hint2 = u"ℹ\nOkno można przeskalowywać"

        self.hintText = QLabel(self.centralwidget)
        self.hintText.setObjectName(u"resizeText")
        self.hintText.setText(hint1 + '\n' + hint2)
        self.hintText.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.hintText)
        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.window_name, None))
    # retranslateUi

if __name__ == "__main__":
    print('Run mainwindow.py or neuron-start.py to start program')