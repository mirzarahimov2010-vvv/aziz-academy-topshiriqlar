n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

category_totals = {}
for item in items:
    cat = item['cat']
    total = item['price'] * item['qty']
    if cat in category_totals:
        category_totals[cat] += total 
    else:
        category_totals[cat] = total 
sorted_categories = sorted(category_totals.keys())
for cat in sorted_categories:
    print(f"{cat} {category_totals[cat]}")