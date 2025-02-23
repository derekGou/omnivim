from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import os

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.layout = QVBoxLayout()
        self.label = QLabel(self)

        pixmap = QPixmap("Images/omnivimtitle.png")  # Replace with actual image path
        self.label.setPixmap(pixmap.scaled(354, 72, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setWindowTitle("Omnivim")
        self.setLayout(self.layout)
        self.extratext = ""
        
        with open("Windows_Mouse_Movments/vimmode.txt", "r") as f:
            typ = f.read().strip()
        
        if typ == "kill" or len(typ) == 0:
            self.extratext = "Turn on"
        else:
            self.extratext = "Turn off"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, "Ibm.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        print(font_family)
        if font_id == -1:
            print("Error: Font not loaded.")
            return
        font = QFont(font_family)

        self.button = QPushButton(f'{self.extratext} Omnivim')
        self.button.setFont(font)

        font.setPointSize(24)
        font.setWeight(900)
        self.text = QLabel('Vim motions, made global')
        self.text.setFont(font)
        self.layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

        self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button.clicked.connect(self.on_button_click)

        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.textbox = QPlainTextEdit(self)
        self.textbox.setPlainText("Try me out!")
        self.layout.addWidget(self.textbox, alignment=Qt.AlignmentFlag.AlignCenter)

    def on_button_click(self):
        # Update the text based on the state
        with open("Windows_Mouse_Movments/vimmode.txt", "w") as f:
            f.truncate(0)
            if self.extratext == "Turn on":
                f.write("normal")
                self.extratext = "Turn off"
            else:
                f.write("kill")
                self.extratext = "Turn on"

        # Update the button text directly without recreating the button
        self.button.setText(f'{self.extratext} Omnivim')

        # Optionally trigger an update if needed
        self.update()

        print("running")

    def paintEvent(self, event):
        # No need to recreate the button here, just call the parent class's paintEvent
        super().paintEvent(event)

def load_stylesheet(filename):
    file = QFile(filename)
    file.open(QFile.OpenModeFlag.ReadOnly)
    stream = QTextStream(file)
    return stream.readAll()

def run_window():
    app = QApplication(sys.argv)
    stylesheet = load_stylesheet("style.css")
    app.setStyleSheet(stylesheet)

    mw = MainWindow()
    mw.resize(1, 400)
    mw.show()
    sys.exit(app.exec())