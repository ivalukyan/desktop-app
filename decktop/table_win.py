from PySide6 import QtWidgets


class TableWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        
        # Настройка окна
        self.setWindowTitle("Таблица с данными")
        self.resize(500, 500)
        
        # Элементы интерфейса
        self.table = QtWidgets.QTableWidget(4, 4)
        self.fill_table()
        
        # Компоновка
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        
    def fill_table(self):
        
        # Тестовые данные 
        data = [
            ["Apple", "Fruit", "Red", "Sweet"],
            ["Carrot", "Vegetable", "Orange", "Crunchy"],
            ["Banana", "Fruit", "Yellow", "Sweet"],
            ["Broccoli", "Vegetable", "Green", "Bitter"],
        ]
        
        # Задаем заголовки для нашей таблицы
        self.table.setHorizontalHeaderLabels(["Name", "Type", "Color", "Taste"])
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(value)
                self.table.setItem(row, col, item)
                