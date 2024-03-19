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
        self.ui.setMouseReleaseReciever(self.changeGridColor)
        pass
        
    def switchCellColor(self, pos: tuple[int, int]):
        """Switches grid color. changes cell color in UI and saved value. If cell is black, switches to white and same in reverse"""
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

    def handleSelectionChanged(self):
        """Handle the itemSelectionChanged signal."""
        selected_items = [extractIndex(x) for x in self.ui.tableWidget.selectedIndexes()]
        #print("Selected items:", selected_items)
        if len(selected_items) > 0:
            self.__cellChanged = selected_items
            return
        self.changeGridColor()

    def changeGridColor(self):
        """Changes color for selected cells"""
        for pixel in self.__cellChanged:
            self.switchCellColor(pixel)
        pass

def extractIndex(modelIdx: QModelIndex) -> tuple[int, int]:
    """.selectedIndexes() returns QModelIndex object. this function extracts column and row number from it."""
    return (modelIdx.column(), modelIdx.row())