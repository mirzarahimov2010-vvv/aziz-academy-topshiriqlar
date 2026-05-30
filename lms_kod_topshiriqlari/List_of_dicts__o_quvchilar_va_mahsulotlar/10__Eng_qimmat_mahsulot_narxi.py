n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
max_price = max(product['price'] for product in products)
print(max_price)