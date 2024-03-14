# -*- coding: utf-8 -*-

# Do not run this file, it's library for another python script

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QVBoxLayout, QTableWidget, QTableWidgetItem, QLCDNumber)


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
        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName(u"tableLayout")
        self.tableLayout.addWidget(self.tableWidget, stretch=6)

        self.tableWidget.setRowCount(self.table_rows)
        self.tableWidget.setColumnCount(self.table_columns)

        for i in range(self.table_columns):
            self.tableWidget.setColumnWidth(i, self.table_colSize)
        for i in range(self.table_rows):
            self.tableWidget.setRowHeight(i, self.table_rowSize)

        # Hide row and column headers
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)

        # event handler
        self.tableWidget.itemSelectionChanged.connect(self.handleSelectionChanged)

        # graph
        #self.graph = FigureCanvas(Figure(figsize=(5, 3))) # graph
        #self.graph.setObjectName(u"graph")
        # graph nav menu
        #self.graph_nav_menu = NavigationToolbar(self.graph, self.centralwidget)
        #self.graph_nav_menu.setObjectName(u"graph_nav_menu")
        #self.graphLayout.addWidget(self.graph_nav_menu)
        #self.graphLayout.addWidget(self.graph)
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

    def changeCellColor(self, row, col, color):
        self.tableWidget.item(row, col).setBackground(QColor(color))

    # TODO if something is selected, change it's state black/white cell. If selected nothing, don't change anything.

    def handleSelectionChanged(self):
        """Handle the itemSelectionChanged signal."""
        selected_items = [extractIndex(x) for x in self.tableWidget.selectedIndexes()]
        print("Selected items:", selected_items)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", self.window_name, None))
    # retranslateUi

    # def fileButtonClicked(self, receiverFunction):
    #     self.fileButton.clicked.connect(receiverFunction)
    #     pass

    # def displayFilePath(self, filepath):
    #     self.filelabel.setText(u"📃Plik:\n  " + filepath + u"\n")
    #     pass
    
    # # the element that allows to choose quantity is called spinner, thus name
    # def neighbourSpinChanged(self, receiverFunction):
    #     self.neighbourSpin.valueChanged.connect(receiverFunction)
    #     #self.neighbourSpin.valueChanged.connect(catchNeighbourSpinChangedExample)
    #     pass
# def catchNeighbourSpinChangedExample(value):
#     print(f"Neighbour spin value is: {value}")

def extractIndex(modelIdx: QModelIndex) -> tuple[int, int]:
    """.selectedIndexes() returns QModelIndex object. this function extracts column and row number from it."""
    return (modelIdx.column(), modelIdx.row())