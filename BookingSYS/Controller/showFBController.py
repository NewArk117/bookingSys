import sys 
sys.path.append( './Entity' )
from fnb import FnB

class ShowFBController:
    def showFBC(self)->bool:
        FBRecord = FnB().showFBRecord()
        if FBRecord == True:
            return True