# Form implementation generated from reading ui file 'second-window.ui'
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
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-image: url(\'C:/Users/ceian/Desktop/dsa-finals/bg-gradient-1.jpg\');")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.selected_directory = QtWidgets.QLabel(parent=self.frame)
        self.selected_directory.setGeometry(QtCore.QRect(280, 150, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.selected_directory.setFont(font)
        self.selected_directory.setStyleSheet("background: none; color: white;")
        self.selected_directory.setObjectName("selected_directory")
        self.select_directory = QtWidgets.QPushButton(parent=self.frame)
        self.select_directory.setGeometry(QtCore.QRect(60, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.select_directory.setFont(font)
        self.select_directory.setStyleSheet("background: #8695bb;\n"
" color: #333462;\n"
"border: 1px solid #333462;\n"
"border-radius: 7px;")
        self.select_directory.setObjectName("select_directory")
        self.file_type = QtWidgets.QLabel(parent=self.frame)
        self.file_type.setGeometry(QtCore.QRect(100, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.file_type.setFont(font)
        self.file_type.setStyleSheet("background: none; color: white;")
        self.file_type.setObjectName("file_type")
        self.choose_file_type = QtWidgets.QComboBox(parent=self.frame)
        self.choose_file_type.setGeometry(QtCore.QRect(200, 230, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.choose_file_type.setFont(font)
        self.choose_file_type.setStyleSheet("background: white;\n"
" color: black;\n"
"border: 1px solid grey;\n"
"border-radius: 7px;\n"
"padding: 5px;")
        self.choose_file_type.setObjectName("choose_file_type")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.choose_file_type.addItem("")
        self.other_files = QtWidgets.QLineEdit(parent=self.frame)
        self.other_files.setGeometry(QtCore.QRect(200, 270, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.other_files.setFont(font)
        self.other_files.setStyleSheet("font-family: \"Helvetica\";\n"
"background: white;\n"
"color: black;\n"
"border: 1px solid gray;\n"
"border-radius: 7px;\n"
"padding: 5px;")
        self.other_files.setObjectName("other_files")
        self.folder_name = QtWidgets.QLabel(parent=self.frame)
        self.folder_name.setGeometry(QtCore.QRect(70, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.folder_name.setFont(font)
        self.folder_name.setStyleSheet("background: none; color: white;")
        self.folder_name.setObjectName("folder_name")
        self.folder_names = QtWidgets.QLineEdit(parent=self.frame)
        self.folder_names.setGeometry(QtCore.QRect(200, 310, 441, 31))
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
        self.add_instruction = QtWidgets.QPushButton(parent=self.frame)
        self.add_instruction.setGeometry(QtCore.QRect(60, 400, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_instruction.setFont(font)
        self.add_instruction.setStyleSheet("background: #8695bb;\n"
" color: #333462;\n"
"border: 1px solid #333462;\n"
"border-radius: 7px;")
        self.add_instruction.setObjectName("add_instruction")
        self.organize_files = QtWidgets.QPushButton(parent=self.frame)
        self.organize_files.setGeometry(QtCore.QRect(60, 440, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.organize_files.setFont(font)
        self.organize_files.setStyleSheet("background: #e8ab9a;\n"
"color: #d25f44;\n"
"border: 2px solid #d25f44;\n"
"border-radius: 7px;")
        self.organize_files.setObjectName("organize_files")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(60, 490, 581, 171))
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
        self.back_button = QtWidgets.QPushButton(parent=self.frame)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background: #e8ab9a;\n"
"color: #d25f44;\n"
"border: 2px solid #d25f44;\n"
"border-radius: 7px;")
        self.back_button.setObjectName("back_button")
        self.AI_Button = QtWidgets.QPushButton(parent=self.frame)
        self.AI_Button.setGeometry(QtCore.QRect(640, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.AI_Button.setFont(font)
        self.AI_Button.setStyleSheet("background: #e8ab9a;\n"
"color: #d25f44;\n"
"border: 2px solid #d25f44;\n"
"border-radius: 7px;")
        self.AI_Button.setObjectName("AI_Button")
        self.title = QtWidgets.QLabel(parent=self.frame)
        self.title.setGeometry(QtCore.QRect(70, 50, 561, 81))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.selected_directory.setText(_translate("Dialog", "No directory selected"))
        self.select_directory.setText(_translate("Dialog", "Select Directory"))
        self.file_type.setText(_translate("Dialog", "File Type:"))
        self.choose_file_type.setItemText(0, _translate("Dialog", ".txt"))
        self.choose_file_type.setItemText(1, _translate("Dialog", ".png"))
        self.choose_file_type.setItemText(2, _translate("Dialog", ".jpg"))
        self.choose_file_type.setItemText(3, _translate("Dialog", ".mp4"))
        self.choose_file_type.setItemText(4, _translate("Dialog", ".mp3"))
        self.choose_file_type.setItemText(5, _translate("Dialog", ".docx"))
        self.choose_file_type.setItemText(6, _translate("Dialog", ".ppt"))
        self.choose_file_type.setItemText(7, _translate("Dialog", ".pdf"))
        self.other_files.setText(_translate("Dialog", "Other file type"))
        self.folder_name.setText(_translate("Dialog", "Folder Name:"))
        self.folder_names.setText(_translate("Dialog", "e.g., PDF Files, Text Files, etc."))
        self.add_instruction.setText(_translate("Dialog", "Add Instruction"))
        self.organize_files.setText(_translate("Dialog", "Organize Files"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Helvetica\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Current Instructions</p></body></html>"))
        self.back_button.setText(_translate("Dialog", "Home"))
        self.AI_Button.setText(_translate("Dialog", "AI"))
        self.title.setText(_translate("Dialog", "AI File Organizer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
