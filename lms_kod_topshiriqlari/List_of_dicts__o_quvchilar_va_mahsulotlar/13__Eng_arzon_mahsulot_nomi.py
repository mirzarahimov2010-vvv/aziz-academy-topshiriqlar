n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
cheapest_product = products[0]
for product in products:
    if product['price'] < cheapest_product['price']:
        cheapest_product = product 
print(cheapest_product['name'])