import os
import shutil
import json
import openai
from PyQt5 import QtWidgets, QtGui, QtCore


class FileOrganizerAI:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        if not os.path.exists(base_directory):
            os.makedirs(base_directory)
        self.instructions_file = os.path.join(base_directory, 'instructions.json')
        self.load_instructions()

    def load_instructions(self):
        if os.path.exists(self.instructions_file):
            with open(self.instructions_file, 'r') as file:
                self.instructions = json.load(file)
        else:
            self.instructions = {}

    def save_instructions(self):
        with open(self.instructions_file, 'w') as file:
            json.dump(self.instructions, file, indent=4)

    def add_instruction(self, file_type, folder_name):
        """Add or update instructions for organizing files of a specific type."""
        self.instructions[file_type] = folder_name
        self.save_instructions()

    def organize_files(self):
        """Organize files in the base directory based on saved instructions."""
        moved_files = []
        for file_name in os.listdir(self.base_directory):
            file_path = os.path.join(self.base_directory, file_name)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1].lower()
                if file_extension in self.instructions:
                    target_folder = os.path.join(self.base_directory, self.instructions[file_extension])

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file_name))
                    moved_files.append(file_name)
        return moved_files

    def display_instructions(self):
        """Return all stored instructions."""
        return self.instructions


class FileOrganizerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AI File Organizer")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #f9f9f9; font-family: Arial; font-size: 12pt;")

        # Main Layout
        layout = QtWidgets.QVBoxLayout()

        # Header
        header_label = QtWidgets.QLabel("AI File Organizer")
        header_label.setAlignment(QtCore.Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 18pt; color: #333; font-weight: bold;")
        layout.addWidget(header_label)

        # Directory Selection
        dir_layout = QtWidgets.QHBoxLayout()
        self.directory_label = QtWidgets.QLabel("No directory selected")
        self.directory_label.setStyleSheet("color: #555;")
        dir_button = QtWidgets.QPushButton("Select Directory")
        dir_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px 10px;")
        dir_button.clicked.connect(self.select_directory)
        dir_layout.addWidget(self.directory_label)
        dir_layout.addWidget(dir_button)
        layout.addLayout(dir_layout)

        # Instruction Input
        form_layout = QtWidgets.QFormLayout()
        self.file_type_input = QtWidgets.QLineEdit()
        self.file_type_input.setPlaceholderText("e.g., .txt")
        self.folder_name_input = QtWidgets.QLineEdit()
        self.folder_name_input.setPlaceholderText("e.g., Text Files")
        self.add_instruction_button = QtWidgets.QPushButton("Add Instruction")
        self.add_instruction_button.setStyleSheet("background-color: #2196F3; color: white;")
        self.add_instruction_button.clicked.connect(self.add_instruction)
        form_layout.addRow("File Type:", self.file_type_input)
        form_layout.addRow("Folder Name:", self.folder_name_input)
        form_layout.addRow(self.add_instruction_button)
        layout.addLayout(form_layout)

        # Organize Files Button
        self.organize_button = QtWidgets.QPushButton("Organize Files")
        self.organize_button.setStyleSheet("background-color: #FF9800; color: white; padding: 5px 10px;")
        self.organize_button.clicked.connect(self.organize_files)
        layout.addWidget(self.organize_button)

        # Instructions Display
        self.instructions_display = QtWidgets.QTextBrowser()
        self.instructions_display.setStyleSheet("border: 1px solid #ddd; padding: 5px; background-color: #fff;")
        layout.addWidget(self.instructions_display)

        # Chat Section
        chat_layout = QtWidgets.QVBoxLayout()
        chat_label = QtWidgets.QLabel("Chat with AI:")
        chat_label.setStyleSheet("font-weight: bold;")
        self.chat_input = QtWidgets.QLineEdit()
        self.chat_input.setPlaceholderText("Ask a question...")
        self.chat_input.returnPressed.connect(self.chat_with_ai)
        self.chat_response = QtWidgets.QTextBrowser()
        self.chat_response.setStyleSheet("border: 1px solid #ddd; padding: 5px; background-color: #fff;")
        chat_layout.addWidget(chat_label)
        chat_layout.addWidget(self.chat_input)
        chat_layout.addWidget(self.chat_response)
        layout.addLayout(chat_layout)

        # Set Layout
        self.setLayout(layout)

        # Organizer Object
        self.organizer = None

    def select_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.organizer = FileOrganizerAI(directory)
            self.directory_label.setText(f"Selected: {directory}")
            self.display_instructions()

    def add_instruction(self):
        if not self.organizer:
            self.show_error("Please select a directory first.")
            return

        file_type = self.file_type_input.text().strip()
        folder_name = self.folder_name_input.text().strip()

        if not file_type or not folder_name:
            self.show_error("Both fields are required.")
            return

        self.organizer.add_instruction(file_type, folder_name)
        self.display_instructions()
        self.file_type_input.clear()
        self.folder_name_input.clear()

    def organize_files(self):
        if not self.organizer:
            self.show_error("Please select a directory first.")
            return

        moved_files = self.organizer.organize_files()
        if moved_files:
            self.chat_response.append(f"Organized files: {', '.join(moved_files)}")
        else:
            self.chat_response.append("No files were organized.")

    def display_instructions(self):
        if self.organizer:
            instructions = self.organizer.display_instructions()
            display_text = "Current Instructions:\n"
            for file_type, folder in instructions.items():
                display_text += f"  - {file_type}: {folder}\n"
            self.instructions_display.setText(display_text)

    def chat_with_ai(self):
        user_message = self.chat_input.text().strip()
        if not user_message:
            self.chat_response.append("Please enter a message.")
            return

        try:
            # Replace YOUR_API_KEY with your OpenAI API key
            openai.api_key = "YOUR_API_KEY"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for a file organizer program."},
                    {"role": "user", "content": user_message},
                ]
            )
            answer = response['choices'][0]['message']['content']
            self.chat_response.append(f"AI: {answer}")
        except Exception as e:
            self.chat_response.append(f"Error: {str(e)}")

        self.chat_input.clear()

    def show_error(self, message):
        error_box = QtWidgets.QMessageBox()
        error_box.setIcon(QtWidgets.QMessageBox.Critical)
        error_box.setText(message)
        error_box.setWindowTitle("Error")
        error_box.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())