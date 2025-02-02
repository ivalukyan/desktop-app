from PySide6 import QtWidgets


class TableWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Таблицы с данными")
        self.resize(800, 600)

        # Создаем QStackedWidget для переключения между таблицами
        self.stacked_widget = QtWidgets.QStackedWidget()

        # Создаем таблицы
        self.table1 = self.create_table(["Наименование материала", "Тип материала",
                                         "Изображение", "Цена", "Количество на складе",
                                         "Минимальное количество", "Количество в упаковке",
                                         "Единица измерения"], [
            ["Apple", "Fruit", "Red", "Sweet"],
            ["Carrot", "Vegetable", "Orange", "Crunchy"],
            ["Banana", "Fruit", "Yellow", "Sweet"],
            ["Broccoli", "Vegetable", "Green", "Bitter"],
        ])

        self.table2 = self.create_table(["Наименование материала", "Возможный поставщик"], [
            ["1", "Alice", "25"],
            ["2", "Bob", "30"],
            ["3", "Charlie", "35"],
        ])

        # Добавляем таблицы в QStackedWidget
        self.stacked_widget.addWidget(self.table1)
        self.stacked_widget.addWidget(self.table2)

        # Создаем кнопки для переключения между таблицами
        self.button_table1 = QtWidgets.QPushButton("Показать таблицу 1")
        self.button_table2 = QtWidgets.QPushButton("Показать таблицу 2")

        # Подключаем кнопки к методам переключения
        self.button_table1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.button_table2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Компоновка
        layout = QtWidgets.QVBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_table1)
        button_layout.addWidget(self.button_table2)
        layout.addLayout(button_layout)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def create_table(self, headers, data):
        """Создает таблицу с заданными заголовками и данными."""
        table = QtWidgets.QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(value)
                table.setItem(row, col, item)

        return table
                