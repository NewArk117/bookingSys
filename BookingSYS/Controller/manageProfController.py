import sys 
sys.path.append( './Entity' )
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Entity')
from profManage import profManage

class manageProfController:
    def manProf(self, stackedWidget):
        self.stackedWidget = stackedWidget
        print("in Controller")
        profManage().fuc(self.stackedWidget)
        