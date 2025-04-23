# Ticket add-ons (VIP, meals, baggage)

# Base Ticket Interface


class Ticket:
    def get_price(self):
        pass

    def get_description(self):
        pass

# Concrete Basic Ticket
class BasicTicket(Ticket):
    def get_price(self):
        return 100.0

    def get_description(self):
        return "Basic Ticket"

# Decorator Base Class
class TicketDecorator(Ticket):
    def __init__(self, ticket: Ticket):
        self._ticket = ticket

    def get_price(self):
        return self._ticket.get_price()

    def get_description(self):
        return self._ticket.get_description()

# Concrete Decorators
class VIPService(TicketDecorator):
    def get_price(self):
        return super().get_price() + 50.0

    def get_description(self):
        return super().get_description() + " + VIP Service"

class ExtraBaggage(TicketDecorator):
    def get_price(self):
        return super().get_price() + 20.0

    def get_description(self):
        return super().get_description() + " + Extra Baggage"

class MealOption(TicketDecorator):
    def get_price(self):
        return super().get_price() + 15.0

    def get_description(self):
        return super().get_description() + " + Meal"

# Example usage
# ticket = BasicTicket()
# ticket = VIPService(ticket)
# ticket = ExtraBaggage(ticket)
# ticket = MealOption(ticket)

# print("Description:", ticket.get_description())
# print("Total Price:", ticket.get_price())
