import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click me!")
        self.table = QtWidgets.QTableWidget(3, 3)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

        # Заполняем таблицу начальными данными
        self.fill_table()

    def fill_table(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QtWidgets.QTableWidgetItem(f"Row {row}, Col {col}")
                self.table.setItem(row, col, item)

    # @QtCore.Slot()
    # def magic(self):
    #     # Обновляем случайную ячейку в таблице
    #     row = random.randint(0, self.table.rowCount() - 1)
    #     col = random.randint(0, self.table.columnCount() - 1)
    #     self.table.setItem(row, col, QtWidgets.QTableWidgetItem("Magic!"))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())