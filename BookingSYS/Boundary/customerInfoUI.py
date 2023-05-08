from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel


#This class shows the record of buying tickets or food
class customerInfoUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('Account Information')
        self.resize(400, 300)

        self.record_button = QPushButton('Ticket Purchase Record', self)
        self.record_button.setGeometry(150, 100, 300, 30)

        self.fnb_record_button = QPushButton('F&B Purchase Record', self)
        self.fnb_record_button.setGeometry(150, 150, 300, 30)

        self.loyalty_button = QPushButton('Loyalty Points', self)
        self.loyalty_button.setGeometry(150, 200, 300, 30)

        self.back_button = QPushButton('Back', self)
        self.back_button.setGeometry(150, 250, 300, 30)

        self.record_button.clicked.connect(self.show_ticket_record_window)
        self.fnb_record_button.clicked.connect(self.show_fnb_record_window)
        self.loyalty_button.clicked.connect(self.show_loyalty_points)
        self.back_button.clicked.connect(self.go_back)

    def show_ticket_record_window(self):
        self.ticket_record_window = QWidget()
        self.ticket_record_window.setWindowTitle('Ticket Purchase Record')
        self.ticket_record_window.resize(400, 300)

        self.ticket_text_box = QTextEdit(self.ticket_record_window)
        self.ticket_delete_button = QPushButton('Refund', self.ticket_record_window)
        self.ticket_update_button = QPushButton('Change', self.ticket_record_window)

        vbox = QVBoxLayout()
        vbox.addWidget(self.ticket_text_box)
        hbox = QHBoxLayout()
        hbox.addWidget(self.ticket_delete_button)
        hbox.addWidget(self.ticket_update_button)
        vbox.addLayout(hbox)
        self.ticket_record_window.setLayout(vbox)

        self.ticket_record_window.show()

    def show_fnb_record_window(self):
        self.fnb_record_window = QWidget()
        self.fnb_record_window.setWindowTitle('F&B Purchase Record')
        self.fnb_record_window.resize(400, 300)

        self.fnb_text_box = QTextEdit(self.fnb_record_window)
        self.fnb_delete_button = QPushButton('Refund', self.fnb_record_window)
        self.fnb_update_button = QPushButton('Change', self.fnb_record_window)

        vbox = QVBoxLayout()
        vbox.addWidget(self.fnb_text_box)
        hbox = QHBoxLayout()
        hbox.addWidget(self.fnb_delete_button)
        hbox.addWidget(self.fnb_update_button)
        vbox.addLayout(hbox)
        self.fnb_record_window.setLayout(vbox)

        self.fnb_record_window.show()

    def show_loyalty_points(self):
        self.loyalty_points_window = QWidget()
        self.loyalty_points_window.setWindowTitle('Loyalty Points')
        self.loyalty_points_window.resize(400, 300)

        self.points_label = QLabel('Your current loyalty points: XXX', self.loyalty_points_window)
        self.points_label.setStyleSheet('font-size: 18px; margin-bottom: 20px;')

        vbox = QVBoxLayout(self.loyalty_points_window)
        vbox.addWidget(self.points_label)
        vbox.setAlignment(Qt.AlignCenter)


        self.loyalty_points_window.show()

    def go_back(self):
        self.stackedWidget.setCurrentIndex(6)













