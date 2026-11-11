class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty 
    def total(self):
        return self.price * self.qty 
    
try:
    name_input = input().strip()
    price_input = int(input())
    qty_input = int(input())
    
    if not name_input or price_input < 0 or qty_input < 0:
        print("BAD")
    else:
        product = Product(name_input, price_input, qty_input)
        print(product.total())
except ValueError:
    print("BAD")