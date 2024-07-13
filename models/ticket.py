
class Ticket:
    def __init__(self, description):
        self.description = description
        self.status = "Pendiente"

class Control:
    def __init__(self, successor=None):
        self.successor = successor

    def control(self, ticket):
        if self.successor:
            return self.successor.control(ticket)
        return None

class Director(Control):
    def control(self, ticket):
        if ticket.description.startswith("Director"):
            ticket.status = "Aprobado por el Director"
            return ticket.status
        else:
            return super().control(ticket)

class Administrativo(Control):
    def control(self, ticket):
        if ticket.description.startswith("Administrativo"):
            ticket.status = "Aprobado por el Administrativo"
            return ticket.status
        else:
            return super().control(ticket)

class Asistente(Control):
    def control(self, ticket):
        if ticket.description.startswith("Asistente"):
            ticket.status = "Aprobado por el Asistente"
            return ticket.status
        else:
            return super().control(ticket)
