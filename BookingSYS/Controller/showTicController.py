import sys 
sys.path.append( './Entity' )
from ticket import ticket

class ShowTicketController:
    def showTicketC(self)->bool:
        ticketRecord = ticket().showTicketRecord()
        if ticketRecord == True:
            return True