from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        MainWindow.setStyleSheet("background-image: url('bg-gradient.jpg');")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Frame
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setObjectName("frame")

        # Title
        self.title = QtWidgets.QLabel(parent=self.frame)
        self.title.setGeometry(QtCore.QRect(60, 240, 561, 81))
        self.title.setFont(QtGui.QFont("Helvetica", 52, QtGui.QFont.Weight.Bold))
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("background: transparent; border: none; color: white;")
        self.title.setObjectName("title")

        # Catchphrase
        self.catchphrase = QtWidgets.QLabel(parent=self.frame)
        self.catchphrase.setGeometry(QtCore.QRect(200, 320, 271, 31))
        self.catchphrase.setFont(QtGui.QFont("Helvetica", 18, italic=True))
        self.catchphrase.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.catchphrase.setStyleSheet("background: transparent; border: none; color: white;")
        self.catchphrase.setObjectName("catchphrase")

        # Start Button
        self.start = QtWidgets.QPushButton(parent=self.frame)
        self.start.setGeometry(QtCore.QRect(220, 390, 241, 41))
        self.start.setFont(QtGui.QFont("Helvetica", 20))
        self.start.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.start.setObjectName("start")

        # Chat AI Button
        self.chat_ai = QtWidgets.QPushButton(parent=self.frame)
        self.chat_ai.setGeometry(QtCore.QRect(220, 440, 241, 41))
        self.chat_ai.setFont(QtGui.QFont("Helvetica", 20))
        self.chat_ai.setStyleSheet("background: #8695bb; color: #333462; border: 1px solid #333462; border-radius: 7px;")
        self.chat_ai.setObjectName("chat_ai")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI File Organizer"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.title.setText(_translate("MainWindow", "AI File Organizer"))
        self.catchphrase.setText(_translate("MainWindow", "Your Files, We Organize"))
        self.chat_ai.setText(_translate("MainWindow", "Chat With AI"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
