first_set = set(input().split())

queries = input().split()

count = 0
for item in queries:
    if item in first_set:
        count += 1 
        
print(count)