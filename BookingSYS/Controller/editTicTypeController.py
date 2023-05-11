import sys 
sys.path.append( './Entity' )
from PyQt5.QtWidgets import QMessageBox
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from ticketType import ticketType

class editTicTypeController:
    def editTicTypeC(self,dialog, stackedwidget, oldname,oldprice, newname, newprice):
        try:
            if newname and newprice:
                ticketType().editTicType(dialog, stackedwidget, oldname,oldprice, newname, newprice)
            else:
                raise ValueError("New columns are empty")
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))