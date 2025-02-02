import sys
import logging
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from decktop.login_form import LoginForm



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    app = QtWidgets.QApplication(sys.argv)
    
    app_icon = QIcon("app.ico")
    app.setWindowIcon(app_icon)

    login_form = LoginForm()
    login_form.show()

    sys.exit(app.exec())