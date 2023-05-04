import sys 
sys.path.append( './Entity' )
from profManage import profManage

class manageProfController:
    def manProf(self, stackedWidget):
        self.stackedWidget = stackedWidget
        profManage().fuc(self.stackedWidget)
        