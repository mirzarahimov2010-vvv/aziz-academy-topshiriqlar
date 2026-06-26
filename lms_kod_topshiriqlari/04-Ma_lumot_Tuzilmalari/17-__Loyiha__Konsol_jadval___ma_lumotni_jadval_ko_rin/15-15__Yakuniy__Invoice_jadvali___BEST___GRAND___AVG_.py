n = int(input())

products = []

for _ in range(n):
    name, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price 
    products.append((name, qty, price, total))
    
max_total = max(p[3] for p in products)

best_candidates = [p for p in products if p[3] == max_total]
best_candidates.sort(key=lambda x: x[0])
best = best_candidates[0]

grand_total = sum(p[3] for p in products)
avg_price = sum(p[2] for p in products) / n 

print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
for product, qty, price, total in products:
    print(f"{product:<12} | {qty:>5} |  {price:>6} |  {total:>8}")
    
print(f"BEST: {best[0]} {best[3]}")
print(f"GRAND: {grand_total}")
print(f"AVG_PRICE: {avg_price:.2f}")