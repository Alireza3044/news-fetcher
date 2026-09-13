from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, \
     QVBoxLayout, QPushButton, QComboBox, QMessageBox
from dialogs import TextDialog, EmailDialog
from news import News
import sys


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Configuation
        self.setWindowTitle("News Fetcher")
        self.setFixedSize(250, 150)
        # Widgets
        label1 = QLabel("Enter a keyword to search for:")
        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("Keyword...")
        label2 = QLabel("In which way do you want to get the news?")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["text", "email"])
        button = QPushButton("Confirm")
        button.clicked.connect(self.confirm)
        # Add widget to layout
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(self.keyword_input)
        layout.addWidget(label2)
        layout.addWidget(self.combo_box)
        layout.addWidget(button)
        # Set layout
        self.setLayout(layout)
    
    def confirm(self) -> None:
        keyword = self.keyword_input.text()
        if keyword:
            news = News.fetch(keyword, "2026-06-20")
            news_text = News.make_html(news)
            
            option = self.combo_box.currentText()
            if option == "text":
                keyword = main_window.keyword_input.text()
                dialog = TextDialog(keyword, news_text)
                dialog.exec()
            else:
                dialog = EmailDialog(keyword, news_text)
                dialog.exec()
        else:
            warning = QMessageBox()
            warning.setWindowTitle("Warning")
            warning.setText("Please enter a keyword.")
            warning.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
