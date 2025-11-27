from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import Qt

from app.services.auth_service import AuthService
from ui.windows.main_window import MainWindow


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evertech - Iniciar Sesión")
        self.setMinimumSize(350, 200)

        layout = QVBoxLayout(self)

        title = QLabel("Iniciar Sesión")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")
        layout.addWidget(self.user_input)

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Contraseña")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.pass_input)

        login_btn = QPushButton("Ingresar")
        login_btn.clicked.connect(self.try_login)
        layout.addWidget(login_btn)

    def try_login(self):
        """Intenta loguear al usuario usando AuthService"""
        username = self.user_input.text().strip()
        password = self.pass_input.text().strip()

        try:
            user_data = AuthService.login(username, password)
            # Login exitoso
            self.open_main_window()
        except ValueError:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
        except ConnectionError:
            QMessageBox.critical(
                self, "Error", "No se pudo conectar a la base de datos"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {e}")

    def open_main_window(self):
        """Abre la ventana principal y cierra el login"""
        self.main_window = MainWindow()
        self.main_window.show()
        self.accept()
