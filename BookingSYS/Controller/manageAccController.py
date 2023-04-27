import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from accManage import accManage

class manageAccController:
    def manAcc(self, stackedWidget):
        self.stackedWidget = stackedWidget
        print("in manage account Controller")
        accManage().fuc(self.stackedWidget)
        