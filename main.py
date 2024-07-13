
from controller.ticket_controller import TicketController

def main():
    controller = TicketController()

    # Crear tickets
    ticket1 = controller.create_ticket("Director: Supervisar al personal")
    ticket2 = controller.create_ticket("Administrativo: Mantener registros e informes actualizados")
    ticket3 = controller.create_ticket("Asistente: Organizar y programar reuniones")

    # Aprobar los tickets
    print(controller.ticket_aprobado(ticket1))  
    print(controller.ticket_aprobado(ticket2))  
    print(controller.ticket_aprobado(ticket3))  

    # Listar todos los tickets y sus estados
    for ticket in controller.list_tickets():
        print(f"Ticket: {ticket.description}, Estado: {ticket.status}")

if __name__ == "__main__":
    main()
