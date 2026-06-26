n = int(input().strip())
numbers = input().strip().split()
result = []
for num_str in numbers:
    if len(num_str) == 1:
        result.append(len(num_str))
    else:
        result.append(len(num_str))
print(result)
