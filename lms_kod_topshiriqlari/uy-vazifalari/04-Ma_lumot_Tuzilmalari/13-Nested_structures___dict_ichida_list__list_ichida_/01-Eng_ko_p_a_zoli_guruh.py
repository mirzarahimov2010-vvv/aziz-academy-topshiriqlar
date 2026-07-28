n = int(input())
groups = {}
max_len = -1
best_group = ""

for _ in range(n):
    line = input().split()
    group_name = line[0]
    members = line[1:]
    
    groups[group_name] = members
    
    if len(members) > max_len:
        max_len = len(members)
        best_group = group_name
        
print(best_group) 