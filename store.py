from products import *

class Store:

    def __init__(self, products_list):
        self.products_list = products_list

    def add_product(self, product):
        if is_product_type_check(product):
            if product not in self.products_list:
                self.products_list.append(product)
            else:
                raise Exception ("product is already in the store")

    def remove_product(self, product):
        if product in self.products_list:
            self.products_list.remove(product)

    def get_total_quantity(self):
        return len(self.products_list)

    def get_all_products(self):
        active_products_list = []
        for product in self.products_list:
            if product.is_active():
                active_products_list.append(product)
        return active_products_list

    def order(self, shopping_list):
        order_price = 0
        if len(shopping_list) > 0:
            for order_tuple in shopping_list:
                if type(order_tuple) is tuple:
                    if is_product_type_check(order_tuple[0]) and is_int_type_check(order_tuple[1]):
                        if order_tuple[0] in self.products_list:
                            order_price += order_tuple[0].buy(order_tuple[1])
                        else:
                            raise Exception("product doesn't exist in the store")
                else:
                    raise Exception("shopping list element is not a tuple!")
            return order_price
        else:
            raise Exception("empty shopping list")

def is_product_type_check(product):
    if type(product) is Product:
        return True
    else:
        raise Exception("This is not an instance of class Product!")
