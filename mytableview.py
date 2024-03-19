from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QVBoxLayout, QTableWidget, QTableWidgetItem, QLCDNumber)

class MyTableView(QTableWidget):
	def setMyMouseReleaseReciever(self, reciever):
		self.myMouseReleaseReciever = reciever
	def mouseReleaseEvent(self, event: QMouseEvent) -> None:
		self.myMouseReleaseReciever()
		return super().mouseReleaseEvent(event)