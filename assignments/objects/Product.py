class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def checkQuantity(self, quantity):
        return self.quantity >= quantity

    def totalCost(self, quantity):
        return self.price * quantity

    def subtractQuantity(self, quantity):
        return self.quantity - quantity
