# Form implementation generated from reading ui file 'third-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-image: url(\'C:/Users/ceian/Desktop/dsa-finals/bg-gradient-1.jpg\');")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(60, 190, 571, 421))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("font-family: \"Helvetica\";\n"
"border: 1px solid gray; \n"
"padding: 5px; \n"
"background: #fff;\n"
"border-radius: 7px;")
        self.textBrowser.setObjectName("textBrowser")
        self.home_button = QtWidgets.QPushButton(parent=self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.home_button.setFont(font)
        self.home_button.setStyleSheet("background: #e8ab9a;\n"
"color: #d25f44;\n"
"border: 2px solid #d25f44;\n"
"border-radius: 7px;")
        self.home_button.setObjectName("home_button")
        self.organize_button = QtWidgets.QPushButton(parent=self.frame)
        self.organize_button.setGeometry(QtCore.QRect(630, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.organize_button.setFont(font)
        self.organize_button.setStyleSheet("background: #e8ab9a;\n"
"color: #d25f44;\n"
"border: 2px solid #d25f44;\n"
"border-radius: 7px;")
        self.organize_button.setObjectName("organize_button")
        self.folder_names = QtWidgets.QLineEdit(parent=self.frame)
        self.folder_names.setGeometry(QtCore.QRect(60, 620, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.folder_names.setFont(font)
        self.folder_names.setStyleSheet("font-family: \"Helvetica\";\n"
"background: white;\n"
"color: black;\n"
"border: 1px solid gray;\n"
"border-radius: 7px;\n"
"padding: 5px;")
        self.folder_names.setObjectName("folder_names")
        self.title = QtWidgets.QLabel(parent=self.frame)
        self.title.setGeometry(QtCore.QRect(60, 50, 561, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(0)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet("background: transparent;\n"
"border: none;\n"
"font-family: \'Helvetica\';\n"
"font-size:70px;\n"
"color: white;")
        self.title.setObjectName("title")
        self.title_2 = QtWidgets.QLabel(parent=self.frame)
        self.title_2.setGeometry(QtCore.QRect(250, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(True)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("background: transparent;\n"
"border: none;\n"
"font-family: \'Helvetica\';\n"
"font-size:30px;\n"
"color: white;")
        self.title_2.setObjectName("title_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Helvetica\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Results</p></body></html>"))
        self.home_button.setText(_translate("Dialog", "Home"))
        self.organize_button.setText(_translate("Dialog", "Organize"))
        self.folder_names.setText(_translate("Dialog", "Ask A Question..."))
        self.title.setText(_translate("Dialog", "AI File Organizer"))
        self.title_2.setText(_translate("Dialog", "Chat With AI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
