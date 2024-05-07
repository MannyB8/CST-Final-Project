from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QScrollArea, QTextEdit, QLineEdit, QPushButton

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Chat Application")
        self.setGeometry(100, 100, 400, 400)
        
        # Main widget to hold messages
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Layout for main widget
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Scroll area for messages
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        
        # Widget to hold messages
        self.messages_widget = QWidget()
        scroll_area.setWidget(self.messages_widget)
        
        # Layout for messages
        self.messages_layout = QVBoxLayout()
        self.messages_widget.setLayout(self.messages_layout)
        
        # Input box for user messages
        self.input_box = QLineEdit()
        main_layout.addWidget(self.input_box)
        
        # Button to submit message
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        main_layout.addWidget(self.send_button)
        
        # Add example messages
        self.add_message("John", "hey")
        self.add_message("Manny", "Hi")

    def add_message(self, sender, message):
        message_edit = QTextEdit()
        message_edit.setReadOnly(True)
        message_edit.setStyleSheet("border: none; background-color: transparent;")
        message_edit.setHtml(f"<b>{sender}:</b> {message}<br>")
        self.messages_layout.addWidget(message_edit)

    def send_message(self):
        message = self.input_box.text()
        if message:
            self.add_message("You", message)
            self.input_box.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec()
