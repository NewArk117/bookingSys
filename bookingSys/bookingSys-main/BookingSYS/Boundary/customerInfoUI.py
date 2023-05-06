
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
#This class shows the record of buying tickets or food
class customerInfoUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('Personal Information')
        self.resize(400, 300)

        self.record_button = QPushButton('Ticket Purchase Record', self)
        self.record_button.setGeometry(150, 150, 300, 30)

        self.record_button.clicked.connect(self.show_record_window)

    def show_record_window(self):
        self.record_window = QWidget()
        self.record_window.setWindowTitle('Ticket Purchase Record')
        self.record_window.resize(400, 300)

        self.text_box = QTextEdit(self.record_window)
        self.delete_button = QPushButton('Delete', self.record_window)
        self.update_button = QPushButton('Update', self.record_window)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_box)
        hbox = QHBoxLayout()
        hbox.addWidget(self.delete_button)
        hbox.addWidget(self.update_button)
        vbox.addLayout(hbox)
        self.record_window.setLayout(vbox)

        self.record_window.show()





