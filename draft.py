from PyQt6 import QtCore, QtGui, QtWidgets
import os
import shutil
import json
import openai

class FileOrganizerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("AI File Organizer")
        self.setGeometry(100, 100, 700, 700)
        self.setStyleSheet("background-image: url(\'C:/Users/ceian/Desktop/dsa-finals/bg-gradient.jpg\');")
        self.frame = QtWidgets.QFrame(parent=self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.start = QtWidgets.QPushButton(parent=self.frame)
        self.start.setGeometry(QtCore.QRect(220, 390, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.start.setObjectName("start")
        self.title = QtWidgets.QLabel(parent=self.frame)
        self.title.setGeometry(QtCore.QRect(60, 240, 561, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(1)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet("background: transparent; border: none; font-family: \'Helvetica\'; font-size:70px; color: white;")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec())

