import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox
sys.path.append('./Boundary')

class logO:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget

        reply = QMessageBox.question(self.stackedWidget, 'Confirm logout',
                                    'Are you sure you want to logout?',
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.stackedWidget.setCurrentIndex(1)