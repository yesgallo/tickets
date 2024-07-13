
from service.ticket_service import TicketService
from service.service_ok import service_ok
from models.ticket import Director, Administrativo, Asistente

class TicketController:
    def __init__(self):
        self.ticket_service = TicketService()
        
        # Crear la cadena de responsabilidad
        self.control_chain = Asistente(Administrativo(Director()))

    def create_ticket(self, description):
        return self.ticket_service.create_ticket(description)

    def ticket_aprobado(self, ticket):
        service_ok = service_ok(self.control_chain)
        return service_ok.ticket_aprobado(ticket)

    def list_tickets(self):
        return self.ticket_service.get_tickets()
