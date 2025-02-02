import sys
from PySide6 import QtWidgets
from decktop.login_form import LoginForm



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    login_form = LoginForm()
    login_form.show()

    sys.exit(app.exec())