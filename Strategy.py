
#Different pricing / payment
# Strategy Interface
class PricingStrategy:
    def calculate_price(self, distance):
        pass

# Concrete Strategies
class EconomyClass(PricingStrategy):
    def calculate_price(self, distance):
        return distance * 0.5

class ACClass(PricingStrategy):
    def calculate_price(self, distance):
        return distance * 1.0

class FirstClass(PricingStrategy):
    def calculate_price(self, distance):
        return distance * 1.5

# Context
class Ticket:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def get_price(self, distance):
        return self.strategy.calculate_price(distance)

# Example usage
ticket = Ticket(FirstClass())
print("First Class Ticket Price:", ticket.get_price(100))  # Output: 150.0

ticket.strategy = EconomyClass()
print("Economy Ticket Price:", ticket.get_price(100))  # Output: 50.0
