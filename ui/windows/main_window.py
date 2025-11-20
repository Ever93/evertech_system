from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout,
    QVBoxLayout, QPushButton, QLabel, QFrame
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evertech System - Panel Principal")
        self.setMinimumSize(900, 600)

        # --- Layout general ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # --- SIDEBAR ---
        sidebar = self.build_sidebar()
        main_layout.addWidget(sidebar)

        # --- CONTENIDO PRINCIPAL ---
        self.main_content = self.build_main_content()
        main_layout.addWidget(self.main_content, stretch=1)

    # ------------------------------------
    #   SIDEBAR (MENU LATERAL)
    # ------------------------------------
    def build_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #1e1e1e; color: white;")
        layout = QVBoxLayout()
        sidebar.setLayout(layout)

        title = QLabel("MENÚ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; padding: 10px;")
        layout.addWidget(title)

        # Botones del menú
        buttons = {
            "Ventas": self.show_sales,
            "Productos": self.show_products,
            "Taller": self.show_workshop,
            "Créditos": self.show_credit,
            "Administración": self.show_admin
        }

        for text, callback in buttons.items():
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2e2e2e;
                    color: white;
                    padding: 10px;
                    border: none;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #3b3b3b;
                }
            """)
            btn.clicked.connect(callback)
            layout.addWidget(btn)

        layout.addStretch()
        return sidebar

    # ------------------------------------
    #   PANEL PRINCIPAL
    # ------------------------------------
    def build_main_content(self):
        frame = QFrame()
        layout = QVBoxLayout()
        frame.setLayout(layout)

        self.title_label = QLabel("Bienvenido a Evertech System")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.title_label)
        layout.addStretch()

        return frame

    # ------------------------------------
    #   MÉTODOS PARA ACTUALIZAR VISTA
    # ------------------------------------
    def update_main_view(self, text):
        self.title_label.setText(text)

    def show_sales(self):
        self.update_main_view("Gestión de Ventas")

    def show_products(self):
        self.update_main_view("Gestión de Productos")

    def show_workshop(self):
        self.update_main_view("Taller - Equipos en Reparación")

    def show_credit(self):
        self.update_main_view("Gestión de Créditos y Cuotas")

    def show_admin(self):
        self.update_main_view("Administración y Reportes")
