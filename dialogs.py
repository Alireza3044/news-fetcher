from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QVBoxLayout, \
    QPushButton, QMessageBox, QTextBrowser
from emailing import Email


class TextDialog(QDialog):
    def __init__(self, keyword: str, html: str) -> None:
        super().__init__()
        # Configuration
        self.setWindowTitle("News")
        self.setMinimumSize(400, 500)
        # Widgets
        text_browser = QTextBrowser()
        text_browser.insertHtml(f"<h1>Today's news on {keyword}<h1>{html}")
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(text_browser)
        self.setLayout(layout)


class EmailDialog(QDialog):
    def __init__(self, keyword: str, html: str) -> None:
        super().__init__()
        # Configuration
        self.setWindowTitle("Email")
        self.setFixedWidth(250)
        self.keyword = keyword
        self.email_html = html
        # Widgets
        label = QLabel("Enter your email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email...")
        button = QPushButton("Confirm")
        button.clicked.connect(self.send_mail)
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.email_input)
        layout.addWidget(button)
        self.setLayout(layout)
    
    def send_mail(self) -> None:
        subject = f"News on {self.keyword}"
        message = self.email_html
        success = QMessageBox()
        
        receiver = self.email_input.text()
        if receiver:
            try:
                Email.send_email(subject, message, receiver)
            except Exception as e:
                error = QMessageBox()
                error.setWindowTitle("Error")
                err_msg = f"Something went wrong during sending the email:{e}"
                error.setText(err_msg)
                error.exec()
            else:
                success.setWindowTitle("Success")
                success.setText("The email has been sent successfully!")
                success.exec()
            finally:
                self.close()
        else:
            success.setWindowTitle("Warning")
            success.setText("Please fill in the receiver email address.")
            success.exec()
