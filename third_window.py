from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(700, 700)
        ThirdWindow.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        ThirdWindow.setStyleSheet("background-image: url('C:/Users/ceian/Desktop/dsa-finals/bg-gradient-1.jpg');")

        # Frame
        self.frame = QtWidgets.QFrame(parent=ThirdWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setObjectName("frame")

        # Title
        self.title = QtWidgets.QLabel(parent=self.frame)
        self.title.setGeometry(QtCore.QRect(60, 50, 561, 81))
        self.title.setFont(QtGui.QFont("Helvetica", 52, QtGui.QFont.Weight.Bold))
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("background: transparent; border: none; font-family: 'Helvetica'; color: white;")
        self.title.setObjectName("title")
        
        # Chat AI
        self.chat_ai = QtWidgets.QLabel(parent=self.frame)
        self.chat_ai.setGeometry(QtCore.QRect(250, 140, 181, 41))
        self.chat_ai.setFont(QtGui.QFont("Helvetica", 20, italic=True))
        self.chat_ai.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chat_ai.setStyleSheet("background: transparent; border: none; font-family: 'Helvetica'; color: white;"
        )
        self.chat_ai.setObjectName("chat_ai")

        # Results Box
        self.Results = QtWidgets.QTextBrowser(parent=self.frame)
        self.Results.setGeometry(QtCore.QRect(60, 190, 571, 421))
        self.Results.setFont(QtGui.QFont("Helvetica", 13))
        self.Results.setStyleSheet("font-family: 'Helvetica'; border: 1px solid gray; padding: 5px; background: #fff; border-radius: 7px;")
        self.Results.setObjectName("Results")

        # Ask Question
        self.ask_question = QtWidgets.QLineEdit(parent=self.frame)
        self.ask_question.setGeometry(QtCore.QRect(60, 620, 571, 41))
        self.ask_question.setFont(QtGui.QFont("Helvetica", 11))
        self.ask_question.setStyleSheet("font-family: 'Helvetica'; background: white; color: black; border: 1px solid gray; border-radius: 7px; padding: 5px;")
        self.ask_question.setObjectName("ask_question")

        # Home Button
        self.home_button = QtWidgets.QPushButton(parent=self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.home_button.setFont(QtGui.QFont("Helvetica", 9))
        self.home_button.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.home_button.setObjectName("home_button")

        # Organize Button
        self.organize_button = QtWidgets.QPushButton(parent=self.frame)
        self.organize_button.setGeometry(QtCore.QRect(630, 10, 61, 21))
        self.organize_button.setFont(QtGui.QFont("Helvetica", 9))
        self.organize_button.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.organize_button.setObjectName("organize_button")

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        ThirdWindow.setWindowTitle("AI File Organizer")
        self.Results.setHtml("<p>Results</p>")
        self.home_button.setText("Home")
        self.organize_button.setText("Organize")
        self.ask_question.setText("Ask A Question...")
        self.title.setText("AI File Organizer")
        self.chat_ai.setText("Chat With AI")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec())