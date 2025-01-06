class Product:
    def __init__(self, name, price, quantity):
        if is_int_type_check(quantity):
            self.quantity = quantity
        elif quantity == 0:
            raise Exception("please enter a quantity larger than 0!")
        if is_int_or_float_type_check(price):
            self.price = price
        if is_str_type_check(name):
            self.name = name
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if is_int_type_check(quantity):
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
        if is_int_type_check(quantity):
            if quantity <= self.quantity:
                self.quantity = self.quantity - quantity
                return quantity * self.price
            elif quantity == 0:
                raise Exception("please give a quantity larger than 0!")
            else:
                raise Exception("not enough quantity in the warehouse°")

def is_int_type_check(num):

    if type(num) is int:
        return True
    else:
        raise Exception("please only enter an integer!")

def is_int_or_float_type_check(num):

    if type(num) is int or float:
        return True
    else:
        raise Exception("please only enter an integer or a float!")

def is_str_type_check(input_str):

    if type(input_str) is str:
        return True
    else:
        raise Exception("please only enter a string!")

