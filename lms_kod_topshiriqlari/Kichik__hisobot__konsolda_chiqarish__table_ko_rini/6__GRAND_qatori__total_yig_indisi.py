n = int(input())

products = []
grand_total = 0 

for _ in range(n):
    product, qty, price = input().strip().rsplit(' ', 2)
    qty = int(qty)
    price = int(price)
    total = qty * price 
    grand_total += total 
    products.append((product, qty, price, total))
    
print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
for product, qty, price, total in products:
    
    
    
    print(f"{product:<12} | {qty:>5} |  {price:>6} |  {total:>8}")
    
print(f"GRAND: {grand_total}")