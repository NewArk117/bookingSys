import sys
sys.path.append( './Entity' )
from ticket import ticket

class TicketController:
    def __init__(self, ticket_purchased_ui):
        self.ticket_purchased_ui = ticket_purchased_ui

    def setUserID(self, user_id):
        self.ticket_purchased_ui.setID(user_id)

    def retrieveUserTickets(self):
        user_id = self.ticket_purchased_ui.userID
        ticket_data = ticket.get_user_tickets(user_id)
        ticket_strings = []
        for row in ticket_data:
            ticket_string = '{:<10}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<30}\t{:<10}\t{:<10}'.format(row[0], row[1],
                                                                                                    row[2], row[3],
                                                                                                    row[4], row[5],
                                                                                                    row[6], row[7])
            ticket_strings.append(ticket_string)
        self.ticket_purchased_ui.ticketList.clear()
        self.ticket_purchased_ui.ticketList.addItems(ticket_strings)

    def deleteTicket(self, ticket_id):
        ticket.delete_ticket(ticket_id)
        self.ticket_purchased_ui.viewData()
