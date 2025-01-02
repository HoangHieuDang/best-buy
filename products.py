class Product:
    def __init__(self, name, price, quantity):
        if type(name) is str:
            self.name = name
        else:
            raise Exception("please enter a string for the name!")
        if type(price) is float or int:
            self.price = price
        else:
            raise Exception("please only enter a number for the price!")
        if type(quantity) is float or int:
            self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantify(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= self.quantity:
            self.quantity = self.quantity - quantity
            return quantity * self.price
        else:
            raise Exception("not enough quantity in the warehouse°")


