from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "purple": "#800080",
}

class ColorIdApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color ID App")

        # Create widgets
        self.color_label = QLabel("Enter a color:")
        self.color_input = QLineEdit()
        self.id_label = QLabel()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.display_color_id)

        layout = QVBoxLayout()
        layout.addWidget(self.color_label)
        layout.addWidget(self.color_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.id_label)

        self.setLayout(layout)

    def display_color_id(self):
        color_name = self.color_input.text().lower()
        color_id = colors.get(color_name)

        if color_id:
            self.id_label.setText(f"Color ID: {color_id}")
        else:
            self.id_label.setText("Invalid color")

if __name__ == "__main__":
    app = QApplication([])
    window = ColorIdApp()
    window.show()
    app.exec()
