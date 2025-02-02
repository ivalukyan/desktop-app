import sys
from PySide6 import QtWidgets, QtCore


class LoginForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Настройка окна
        self.setWindowTitle("Форма авторизации")
        self.resize(300, 300)
        
        # Создаем элемент интерфейса
        self.username_label = QtWidgets.QLabel("Логин:")
        self.username_input = QtWidgets.QLineEdit()
        self.password_label = QtWidgets.QLabel("Пароль:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password) # Срываем пароль
        self.login_button = QtWidgets.QPushButton("Выйти")
        self.message_label = QtWidgets.QLabel("")
        
        # Компановка компоненетов
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message_label)
        self.setLayout(layout)
        
    def check_credentials(self):
        # Полученные данные
        username = self.username_input.text() # Добавить проверку поля
        password = self.password_input.text() # Добавить проверку поля
        
        if username == "admin" and password == "123456": # Проверка авторизации пользователя с помощью функции
            self.message_label.setText("Успеный вход!")
            self.message_label.setStyleSheet("color: green")
            
            self.close()
            self.table_window = TableWindow() # Перенаправление на окно с таблицей
            self.table_window.show()
            
        else:
            self.message_label.setText("Нерверный логин или пароль!")
            self.message_label.setStyle("color: red")
