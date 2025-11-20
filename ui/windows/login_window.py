from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt

from ui.windows.main_window import MainWindow   # << IMPORT CORRECTO


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evertech - Iniciar Sesión")
        self.setMinimumSize(350, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("Iniciar Sesión")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Usuario
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")
        layout.addWidget(self.user_input)

        # Contraseña
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Contraseña")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.pass_input)

        # Btn ingresar
        login_btn = QPushButton("Ingresar")
        login_btn.clicked.connect(self.try_login)
        layout.addWidget(login_btn)

    # --------------------------------------------------
    #       VALIDAR LOGIN Y ABRIR MAIN WINDOW
    # --------------------------------------------------
    def try_login(self):

        user = self.user_input.text().strip()
        password = self.pass_input.text().strip()

        # ---------- VALIDACIÓN PROTOTIPO ----------
        # Luego lo reemplazamos por auth_service con PostgreSQL
        if user == "admin" and password == "1234":
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def open_main_window(self):
        """
        Abre el panel principal del sistema y cierra el login.
        """
        self.main_window = MainWindow()     # << Crear la ventana principal
        self.main_window.show()             # << Mostrar la ventana

        self.accept()                       # << Cerrar el login correctamente
