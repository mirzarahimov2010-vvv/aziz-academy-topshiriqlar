n = int(input().strip())
products = []
for _ in range(n):
    product, qty, price = input().strip().rsplit(' ', 2)
    qty = int(qty)
    price = int(price)
    total = qty * price 
    products.append((product, qty, price, total))
    
X = int(input().strip())

filtered = [(p, q, pr, t) for p, q, pr, t in products if t >= X]

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")

if not filtered:
    print("EMPTY")
else:
    for product, qty, price, total in filtered:
        print(f"{product:<12} | {qty:>5} |  {price:>6} |  {total:>8}")