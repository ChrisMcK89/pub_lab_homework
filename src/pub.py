class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []

    def add_drink_to_pub(self, drink):
        self.drink.append(drink)

