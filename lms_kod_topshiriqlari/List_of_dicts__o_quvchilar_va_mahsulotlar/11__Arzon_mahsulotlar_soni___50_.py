n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
count = 0  
for product in products:
    if product['price'] < 50:
        count += 1 
print(count)