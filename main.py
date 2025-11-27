import sys
from PyQt6.QtWidgets import QApplication
from ui.windows.login_window import LoginWindow


def main():
    app = QApplication(sys.argv)  # Ahora QAplication está definido

    login = LoginWindow()
    if login.exec():  # Si login es correcto
        sys.exit(app.exec())
    else:
        sys.exit()


if __name__ == "__main__":
    main()
