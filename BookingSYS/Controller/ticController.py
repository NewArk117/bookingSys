import sys 
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from ticket import ticket

class purchaseTicController:
    def purchaseTicC(self, stackedwidget, list):
        ticket().purchaseTic(stackedwidget, list)

class getTicController:
    def getTicC(self, number):
        return ticket().getTic(number)
