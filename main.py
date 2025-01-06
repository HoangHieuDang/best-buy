import products
from store import *

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
all_products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(all_products[0], 1), (all_products[1], 2)]))