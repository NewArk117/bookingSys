import sys 
sys.path.append( './Entity' )
from owner import owner

class viewHourlyTicController:
    def viewHourlyTicC(self) -> str:
        text,itemname = owner().viewHourlyTic()
        return text, itemname

class viewHourlyRevController:
    def viewHourlyRevC(self) -> str:
        text,itemname = owner().viewHourlyRev()
        return text, itemname
    
class viewDailyTicController:
    def viewDailyTicC(self) -> str:
        text,itemname = owner().viewDailyTic()
        return text, itemname

class viewDailyRevController:
    def viewDailyRevC(self) -> str:
        text,itemname = owner().viewDailyRev()
        return text, itemname
    

class viewWeeklyTicController:
    def viewWeeklyTicC(self) -> str:
        text,itemname = owner().viewWeeklyTic()
        return text, itemname

class viewWeeklyRevController:
    def viewWeeklyRevC(self) -> str:
        text,itemname = owner().viewWeeklyRev()
        return text, itemname