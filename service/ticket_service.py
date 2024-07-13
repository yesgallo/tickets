
from models.ticket import Ticket

class TicketService:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, description):
        ticket = Ticket(description)
        self.tickets.append(ticket)
        return ticket

    def get_tickets(self):
        return self.tickets
