#Import allows execute python script in another python script
import subprocess

#GUI imports
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget, QHBoxLayout

#Import links to different scripts in Boundary
import sys
sys.path.append('./Boundary')
from loginUI import loginUI
from adminUI import adminUI
from customerInfoUI import customerInfoUI
from customerUI import customerUI
from manageAcc import manageAcc
from createAccUI import createAccUI
from createProfUI import createProfUI
from purchaseUI import purchaseUI

#Main class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set the window properties
        self.resize(600,600)
        self.setWindowTitle('Silver Village Inc')

        #Stackedwidget to move from page to page
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        #Main page
        #Title
        title = QLabel(self)
        pixmap = QPixmap('SilverVillageTitle.png')
        title.setPixmap(pixmap)

        #Admin button
        adminButton = QPushButton('Admin')
        adminButton.setMinimumSize(200, 30)
        adminButton.clicked.connect(self.adminLog)
       
        #Customer button
        custButton = QPushButton('Customer')
        custButton.setMinimumSize(200, 30)
        custButton.clicked.connect(self.cusLog)

        #Button layout and initalization
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(QLabel('Login As:'))
        self.hlayout.addWidget(adminButton)
        self.hlayout.addWidget(custButton)

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(title)
        self.vlayout.addStretch()
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addStretch()

        self.pageMain = QWidget()
        self.pageMain.setLayout(self.vlayout)
        self.stackedWidget.addWidget(self.pageMain)

        #Create the object of GUI here
        self.pageLogin = loginUI(self.stackedWidget) #1
        self.stackedWidget.addWidget(self.pageLogin)

        self.admin = adminUI(self.stackedWidget)#2
        self.stackedWidget.addWidget(self.admin)

        self.manageAcc = manageAcc(self.stackedWidget)#3
        self.stackedWidget.addWidget(self.manageAcc)

        self.createAccUI = createAccUI(self.stackedWidget)#4
        self.stackedWidget.addWidget(self.createAccUI)

        self.createProfUI = createProfUI(self.stackedWidget)#5
        self.stackedWidget.addWidget(self.createProfUI)

        self.customerUI = customerUI(self.stackedWidget) #6
        self.stackedWidget.addWidget(self.customerUI)

        self.purchaseUI = purchaseUI(self.stackedWidget)#7
        self.stackedWidget.addWidget(self.purchaseUI)

        self.customerInfoUI = customerInfoUI(self.stackedWidget) #8
        self.stackedWidget.addWidget(self.customerInfoUI)

    #Go to admin login page
    def adminLog(self):
        self.stackedWidget.setCurrentWidget(self.pageLogin)
        self.pageLogin.acctype = "admin"

    def cusLog(self):
        self.stackedWidget.setCurrentWidget(self.pageLogin)
        self.pageLogin.acctype = "customer"

if __name__ == '__main__':
    subprocess.run(["python", "SilverVillageDB.py"])
    subprocess.run(["python", "testData.py"])
    app = QApplication(sys.argv)
    window = MainWindow()
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    window.setPalette(palette)
    window.show()
    sys.exit(app.exec_())