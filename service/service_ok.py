
class service_ok:
    def __init__(self, control):
        self.control = control

    def ticket_aprobado(self, ticket):
        return self.control.control(ticket)
