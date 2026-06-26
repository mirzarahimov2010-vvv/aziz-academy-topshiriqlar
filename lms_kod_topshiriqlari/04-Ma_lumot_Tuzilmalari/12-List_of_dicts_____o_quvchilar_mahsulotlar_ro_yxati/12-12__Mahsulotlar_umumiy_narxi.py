n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
total_price = 0 
for product in products:
    total_price += product['price']
print(total_price)