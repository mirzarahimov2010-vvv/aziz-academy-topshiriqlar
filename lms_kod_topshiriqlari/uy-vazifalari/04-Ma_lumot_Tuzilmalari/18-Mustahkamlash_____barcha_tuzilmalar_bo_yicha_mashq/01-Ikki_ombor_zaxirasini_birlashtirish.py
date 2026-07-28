inventory = {}

n = int(input())
for _ in range(n):
    item, count = input().split()
    inventory[item] = inventory.get(item, 0) + int(count)
    
m = int(input())
for _ in range(m):
    item, count = input().split()
    inventory[item] = inventory.get(item, 0) + int(count)
    
for item in sorted(inventory.keys()):
    print(f"{item} {inventory[item]}")