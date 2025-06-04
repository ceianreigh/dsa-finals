from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(700, 700)
        SecondWindow.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))
        SecondWindow.setStyleSheet("background-image: url('C:/Users/ceian/Desktop/dsa-finals/bg-gradient-1.jpg');")

        # Frame
        self.frame = QtWidgets.QFrame(SecondWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.frame.setObjectName("frame")

        # Title
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(70, 50, 561, 81))
        self.title.setFont(QtGui.QFont("Helvetica", 52, QtGui.QFont.Weight.Bold))
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("background: transparent; color: white;")
        self.title.setObjectName("title")

        # Select Directory
        self.select_directory = QtWidgets.QPushButton(self.frame)
        self.select_directory.setGeometry(QtCore.QRect(60, 150, 211, 31))
        self.select_directory.setFont(QtGui.QFont("Helvetica", 15))
        self.select_directory.setStyleSheet("background: #8695bb; color: #333462; border: 1px solid #333462; border-radius: 7px;")
        self.select_directory.setObjectName("select_directory")

        # Selected Directory
        self.selected_directory = QtWidgets.QLabel(self.frame)
        self.selected_directory.setGeometry(QtCore.QRect(280, 150, 361, 31))
        self.selected_directory.setFont(QtGui.QFont("Helvetica", 20))
        self.selected_directory.setStyleSheet("background: none; color: white;")
        self.selected_directory.setObjectName("selected_directory")

        # File Type
        self.file_type = QtWidgets.QLabel(self.frame)
        self.file_type.setGeometry(QtCore.QRect(100, 230, 91, 31))
        self.file_type.setFont(QtGui.QFont("Helvetica", 14))
        self.file_type.setStyleSheet("background: none; color: white;")
        self.file_type.setObjectName("file_type")

        # Choose File Type
        self.choose_file_type = QtWidgets.QComboBox(self.frame)
        self.choose_file_type.setGeometry(QtCore.QRect(200, 230, 441, 31))
        self.choose_file_type.setFont(QtGui.QFont("Helvetica", 10))
        self.choose_file_type.setStyleSheet("background: white; color: black; border: 1px solid grey; border-radius: 7px; padding: 5px;")
        self.choose_file_type.setObjectName("choose_file_type")
        self.choose_file_type.addItems([".txt", ".png", ".jpg", ".mp4", ".mp3", ".docx", ".ppt", ".pdf"])
        
        # Other File Type
        self.other_files = QtWidgets.QLineEdit(self.frame)
        self.other_files.setGeometry(QtCore.QRect(200, 270, 441, 31))
        self.other_files.setFont(QtGui.QFont("Helvetica", 11))
        self.other_files.setStyleSheet("background: white; color: black; border: 1px solid gray; border-radius: 7px; padding: 5px;")
        self.other_files.setObjectName("other_files")

        # Folder Name
        self.folder_name = QtWidgets.QLabel(self.frame)
        self.folder_name.setGeometry(QtCore.QRect(70, 310, 121, 31))
        self.folder_name.setFont(QtGui.QFont("Helvetica", 14))
        self.folder_name.setStyleSheet("background: none; color: white;")
        self.folder_name.setObjectName("folder_name")

        # Folder Names
        self.folder_names = QtWidgets.QLineEdit(self.frame)
        self.folder_names.setGeometry(QtCore.QRect(200, 310, 441, 31))
        self.folder_names.setFont(QtGui.QFont("Helvetica", 11))
        self.folder_names.setStyleSheet("background: white; color: black; border: 1px solid gray; border-radius: 7px; padding: 5px;")
        self.folder_names.setObjectName("folder_names")

        # Add Instruction Button
        self.add_instruction = QtWidgets.QPushButton(self.frame)
        self.add_instruction.setGeometry(QtCore.QRect(60, 400, 581, 31))
        self.add_instruction.setFont(QtGui.QFont("Helvetica", 15))
        self.add_instruction.setStyleSheet("background: #8695bb; color: #333462; border: 1px solid #333462; border-radius: 7px;")
        self.add_instruction.setObjectName("add_instruction")

        # Organize Files Button
        self.organize_files = QtWidgets.QPushButton(self.frame)
        self.organize_files.setGeometry(QtCore.QRect(60, 440, 581, 31))
        self.organize_files.setFont(QtGui.QFont("Helvetica", 15))
        self.organize_files.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.organize_files.setObjectName("organize_files")

        # Instructions
        self.Instructions = QtWidgets.QTextBrowser(self.frame)
        self.Instructions.setGeometry(QtCore.QRect(60, 490, 581, 171))
        self.Instructions.setFont(QtGui.QFont("Helvetica", 13))
        self.Instructions.setStyleSheet("background: white; border: 1px solid gray; padding: 5px; border-radius: 7px;")
        self.Instructions.setObjectName("Instructions")

        # Home Button
        self.home_button = QtWidgets.QPushButton(self.frame)
        self.home_button.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.home_button.setFont(QtGui.QFont("Helvetica", 9))
        self.home_button.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.home_button.setObjectName("home_button")

        # AI Button
        self.AI_Button = QtWidgets.QPushButton(self.frame)
        self.AI_Button.setGeometry(QtCore.QRect(640, 10, 51, 20))
        self.AI_Button.setFont(QtGui.QFont("Helvetica", 9))
        self.AI_Button.setStyleSheet("background: #e8ab9a; color: #d25f44; border: 2px solid #d25f44; border-radius: 7px;")
        self.AI_Button.setObjectName("AI_Button")

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "AI File Organizer"))
        self.selected_directory.setText(_translate("SecondWindow", "No directory selected"))
        self.select_directory.setText(_translate("SecondWindow", "Select Directory"))
        self.file_type.setText(_translate("SecondWindow", "File Type:"))
        self.other_files.setText(_translate("SecondWindow", "Other file type"))
        self.folder_name.setText(_translate("SecondWindow", "Folder Name:"))
        self.folder_names.setText(_translate("SecondWindow", "e.g., PDF Files, Text Files, etc."))
        self.add_instruction.setText(_translate("SecondWindow", "Add Instruction"))
        self.organize_files.setText(_translate("SecondWindow", "Organize Files"))
        self.home_button.setText(_translate("SecondWindow", "Home"))
        self.Instructions.setHtml(_translate("SecondWindow", "Instructions will be displayed here."))
        self.AI_Button.setText(_translate("SecondWindow", "AI"))
        self.title.setText(_translate("SecondWindow", "AI File Organizer"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec())
