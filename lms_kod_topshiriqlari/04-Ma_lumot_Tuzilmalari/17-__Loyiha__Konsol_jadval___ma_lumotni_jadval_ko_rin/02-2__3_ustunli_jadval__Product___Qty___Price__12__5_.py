n = int(input())
products = []

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    products.append((product, qty, price))
    
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7}")
print(f"{'-'*12}+{'-'*5}+{'-'*7}")

for product, qty, price in products:
    print(f"{product:<12} | {qty:>5} | {price:>7}")