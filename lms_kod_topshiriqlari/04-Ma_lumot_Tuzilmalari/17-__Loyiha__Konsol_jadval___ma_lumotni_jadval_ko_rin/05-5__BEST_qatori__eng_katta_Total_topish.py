n = int(input())

products = []

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price 
    products.append((product, qty, price, total))
    
    
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print(f"{'-'*12}+{'-'*5}+{'-'*7}+{'-'*9}")
 
    
for product, qty, price, total in products:
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
    
    
best_product = None 
best_total = -1 

for product, qty, price, total in products:
    if total > best_total:
        best_total = total 
        best_product = product 
    elif total == best_total:
        if product < best_product:
            
        	best_product = product
        
print(f"BEST: {best_product} {best_total}")
        