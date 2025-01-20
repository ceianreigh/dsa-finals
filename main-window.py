# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-image: url(\'C:/Users/ceian/Desktop/dsa-finals/bg-gradient.jpg\');")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.start = QtWidgets.QPushButton(parent=self.frame)
        self.start.setGeometry(QtCore.QRect(220, 390, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("background: #e8ab9a;\n"
"color: #d25f44;\n"
"border: 2px solid #d25f44;\n"
"border-radius: 7px;")
        self.start.setCheckable(False)
        self.start.setAutoRepeat(False)
        self.start.setAutoDefault(False)
        self.start.setDefault(False)
        self.start.setObjectName("start")
        self.title = QtWidgets.QLabel(parent=self.frame)
        self.title.setGeometry(QtCore.QRect(60, 240, 561, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(1)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet("background: transparent;\n"
"border: none;\n"
"font-family: \'Helvetica\';\n"
"font-size:70px;\n"
"color: white;")
        self.title.setObjectName("title")
        self.catchphrase_2 = QtWidgets.QLabel(parent=self.frame)
        self.catchphrase_2.setGeometry(QtCore.QRect(200, 320, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(True)
        self.catchphrase_2.setFont(font)
        self.catchphrase_2.setStyleSheet("background: transparent;\n"
"border: none;\n"
"font-family: \'Helvetica\';\n"
"font-size: 25px;\n"
"color: white;")
        self.catchphrase_2.setObjectName("catchphrase_2")
        self.chat_ai = QtWidgets.QPushButton(parent=self.frame)
        self.chat_ai.setGeometry(QtCore.QRect(220, 440, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.chat_ai.setFont(font)
        self.chat_ai.setAutoFillBackground(False)
        self.chat_ai.setStyleSheet("background: #8695bb;\n"
" color: #333462;\n"
"border: 1px solid #333462;\n"
"border-radius: 7px;")
        self.chat_ai.setCheckable(False)
        self.chat_ai.setAutoRepeat(False)
        self.chat_ai.setAutoDefault(False)
        self.chat_ai.setDefault(False)
        self.chat_ai.setObjectName("chat_ai")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.start.clicked.connect(self.start.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.title.setText(_translate("MainWindow", "AI File Organizer"))
        self.catchphrase_2.setText(_translate("MainWindow", "Your Files, We Organize"))
        self.chat_ai.setText(_translate("MainWindow", "Chat With AI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
