n = int(input().strip())

data = []
for _ in range(n):
    key, value = input().strip().rsplit(' ', 1)
    value = int(value)
    data.append((key, value))
    
    
print("Key          |        Value")
print("------------+------------")

for key, value in data:
    print(f"{key:<12} |{value:>12}")