from ui_form import Ui_MainWindow

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

# manage ui signals, trigger actions for UI_MainWindow
class UIManager:
    ui: Ui_MainWindow
    grid = [0, 0, 0, 0, 0, 0, 0] # 7
    __cellChanged: list[tuple[int, int]] = list()

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

		# receiver functions should be provided
        self.ui.connectHandleSelectionChanged(self.handleSelectionChanged)
        self.ui.setMouseReleaseReciever(self.mouseReleased)
        self.ui.detectCheckbox.stateChanged.connect(self.handleCheckbox)
        self.ui.detectButt.pressed.connect(self.handleDetectButton)
        self.ui.cleanButt.pressed.connect(self.handleCleanButt)
        pass

    # TODO detectDigit() Don't do it here, pass parameters to some neuralnet manager
    def detectDigit(self):
        print(u"Wykrywanko 🔎...")
        pass

    # UI event handling

    def handleSelectionChanged(self):
        """Handle the itemSelectionChanged signal."""
        selected_items = [extractIndex(x) for x in self.ui.tableWidget.selectedIndexes()]
        #print("Selected items:", selected_items)
        if len(selected_items) > 0:
            self.__cellChanged = selected_items
            return
        self.changeGridColor()
        self.printGrid()
        # detectCheckbox.isChecked() does not return correct value.
        #if self.ui.detectCheckbox.isChecked():
        #    self.detectDigit()
        #if self.ui.detectCheckbox.checkState() == Qt.CheckState.Checked:
            #self.detectDigit()
        #print("selection!")

    def mouseReleased(self):
        """Handle mouse release"""
        # intuition tells me that both handleSelection(nothing selected) and mouse release would do same thing twice, which would be incorrect.
        #  But it's happening only once. Why is that?
        self.changeGridColor()
        self.printGrid()
        if self.ui.detectCheckbox.isChecked():
            self.detectDigit()
        #print("mouse!")
        pass

    def handleCheckbox(self): # probably won't be used
        pass

    def handleDetectButton(self):
        self.detectDigit()
        pass

    def handleCleanButt(self):
        """Handle Clean Button onclick. Basically resets the grid."""
        for x in range(5):
            for y in range(7):
                self.ui.tableWidget.item(y, x).setBackground(QColor("white"))
        self.grid = [0, 0, 0, 0, 0, 0, 0]
        #print("I have clean butt.")
        if self.ui.detectCheckbox.isChecked():
            self.detectDigit()
        pass


    # UI state changing

    def __switchCellColor(self, pos: tuple[int, int]):
        """Switches cell color in grid. changes cell color in UI and stored value. If cell is black, switches to white and same in reverse"""
        col = pos[0]
        row = pos[1]
        if not (row >= 0 and row < 8 and col >= 0 and col < 5):
            return
        access = 1 << col
        color = "black"
        if (self.grid[row] & access) > 0: # it was on (black), switch off (white)
            color = "white"
        self.grid[row] = self.grid[row] ^ access # will change bit, where access has 1.

        # change cell color in UI
        self.ui.tableWidget.item(row, col).setBackground(QColor(color))
        pass

    def changeGridColor(self):
        """Changes color for selected cells"""
        for pixel in self.__cellChanged:
            self.__switchCellColor(pixel)
        pass

    def __getGridAsString(self) -> str:
        text = ""
        for x in self.grid:
            text += str(x) + " "
        return text.rstrip()
    
    def printGrid(self):
        self.ui.digitText.setText("Zakodowana cyfra do skopiowania:\n" + self.__getGridAsString())

    # TODO setDigitsOnLCD()
    def setDigitsOnLCD(self, digits: list[int]):
        pass

def extractIndex(modelIdx: QModelIndex) -> tuple[int, int]:
    """.selectedIndexes() returns QModelIndex object. this function extracts column and row number from it."""
    return (modelIdx.column(), modelIdx.row())