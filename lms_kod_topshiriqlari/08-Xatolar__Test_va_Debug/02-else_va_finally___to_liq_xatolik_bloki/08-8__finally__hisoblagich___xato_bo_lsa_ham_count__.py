n = int(input())
success_count = 0 
total_count = 0 

for _ in range(n):
    total_count += 1
    try:
        x = int(input())
    except ValueError:
        pass 
    else:
        success_count += 1
        
print(f"success {success_count}")
print(f"total {total_count}")