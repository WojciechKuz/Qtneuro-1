# -*- coding: utf-8 -*-

# Do not run this file, it's library for another python script

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
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
        self.lcdLabel.setText(u"Tu wyświetli się wykryta cyfra ⬆\nJeśli nic nie wykryto, wyświetli kropkę")
        self.lcdLabel.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.lcdLabel)

        # widget for spacing
        self.spaceWidget = QWidget(self.centralwidget)
        self.spaceWidget.setObjectName(u"spaceWidget")
        self.verticalLayout.addWidget(self.spaceWidget)

        self.resizeText = QLabel(self.centralwidget)
        self.resizeText.setObjectName(u"resizeText")
        self.resizeText.setText(u"\nOkno można przeskalowywać")
        self.resizeText.setSizePolicy(labelPolicy)
        self.verticalLayout.addWidget(self.resizeText)
        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.window_name, None))
    # retranslateUi