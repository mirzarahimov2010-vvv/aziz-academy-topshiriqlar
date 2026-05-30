n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
sorted_products = sorted(products, key=lambda x: x['price'])
for product in sorted_products:
    print(product['name'], product['price'])