numbers = input().split()

counts = {}

for num in numbers:
    counts[num] = counts.get(num, 0) + 1 
    
mode = max(counts, key=counts.get)

print(mode)