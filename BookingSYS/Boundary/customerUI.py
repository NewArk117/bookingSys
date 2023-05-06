from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,  QVBoxLayout
from logOutController import logOutController

class customerUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()
        self.stackedWidget = stackedWidget

        self.setWindowTitle('SilverVillage Movie')
        self.resize(600, 400)

        self.buy_button = QPushButton('Purchase Movie Tickets')
        self.buy_button.clicked.connect(self.buy_movie_tickets)

        self.info_button = QPushButton('Personal Information')
        self.info_button.clicked.connect(self.show_personal_info)

        self.logout_button = QPushButton('Logout')
        self.logout_button.clicked.connect(self.logOut)


        layout = QVBoxLayout()
        layout.addWidget(self.buy_button)
        layout.addWidget(self.info_button)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def buy_movie_tickets(self):
        self.stackedWidget.setCurrentIndex(7)

    def show_personal_info(self):
        self.stackedWidget.setCurrentIndex(8)

    def logOut(self):
        logOutController.loggingOut(self, self.stackedWidget)
