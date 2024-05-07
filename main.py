import sys
import csv
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(self.size())

        self.ui.stackedWidget.setCurrentWidget(self.ui.login)

        self.ui.login_signup_button.clicked.connect(self.showSignup)
        self.ui.signup_signup_button.clicked.connect(self.signup)
        self.ui.signup_login_button.clicked.connect(self.showLogin)
        self.ui.login_login_button.clicked.connect(self.login)

        self.ui.text_box.returnPressed.connect(self.displayText)

        self.users_file = 'users.csv'

        self.ui.display_box.setReadOnly(True)

    def showSignup(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sign_up)

    def showLogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)

    def signup(self):
        email = self.ui.signup_email.text()
        password = self.ui.signup_password.text()
        username = self.ui.username.text()

        with open(self.users_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == email:
                    QMessageBox.warning(self, "Email in Use",
                                        "This email is already in use. Please use a different email.")
                    return
                if row[2] == username:
                    QMessageBox.warning(self, "Username in Use",
                                        "This username is already in use. Please choose a different username.")
                    return

        if email and password and username:
            with open(self.users_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([email, password, username])
            self.showLogin()
        else:
            QMessageBox.warning(self, "Incomplete Signup", "Please fill in all fields to sign up.")
            pass

    def login(self):
        email = self.ui.login_email.text()
        password = self.ui.login_password.text()

        with open(self.users_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == email and row[1] == password:
                    self.ui.stackedWidget.setCurrentWidget(self.ui.home)
                    return

        QMessageBox.warning(self, "Invalid Login", "Invalid email or password. Please try again or sign up.")

        self.ui.login_email.clear()
        self.ui.login_password.clear()
        pass

    def displayText(self):
        text = self.ui.text_box.text()
        username = "User"
        if self.ui.stackedWidget.currentWidget() == self.ui.home:
            with open(self.users_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == self.ui.login_email.text():
                        username = row[2]

        formatted_text = f"{username}: {text}\n"
        current_text = self.ui.display_box.toPlainText()
        
        new_text = current_text + formatted_text
        self.ui.display_box.setPlainText(new_text)
        self.ui.text_box.clear()

        scrollbar = self.ui.display_box.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
