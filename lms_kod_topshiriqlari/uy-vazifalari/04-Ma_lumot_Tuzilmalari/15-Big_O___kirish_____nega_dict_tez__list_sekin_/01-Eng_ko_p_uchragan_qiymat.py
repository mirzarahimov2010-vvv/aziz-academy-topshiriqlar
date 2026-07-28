items = input().split()

counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1 
    
most_frequent = None
max_count = 0 

for item in items:
    if counts[item] > max_count:
        max_count = counts[item]
        most_frequent = item 
        
print(most_frequent)
        