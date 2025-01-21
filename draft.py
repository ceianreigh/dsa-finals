import sys
from PyQt6 import QtWidgets
from main_window import Ui_MainWindow  # Import Main Window
from second_window import Ui_Dialog as SecondWindow  # Import Second Window
from third_window import Ui_Dialog as ThirdWindow  # Import Third Window


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Main Window Setup
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.start.clicked.connect(self.open_second_window)
        self.main_ui.chat_ai.clicked.connect(self.open_third_window)

        # Initialize other windows
        self.second_window = SecondWindowApp(self)
        self.third_window = ThirdWindowApp(self)

    def open_second_window(self):
        self.hide()
        self.second_window.show()

    def open_third_window(self):
        self.hide()
        self.third_window.show()


class SecondWindowApp(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = SecondWindow()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.back_to_main)
        self.ui.AI_Button.clicked.connect(self.open_third_window)

    def back_to_main(self):
        self.hide()
        self.parent().show()

    def open_third_window(self):
        self.hide()
        self.parent().third_window.show()


class ThirdWindowApp(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ThirdWindow()
        self.ui.setupUi(self)
        self.ui.home_button.clicked.connect(self.back_to_main)

    def back_to_main(self):
        self.hide()
        self.parent().show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
