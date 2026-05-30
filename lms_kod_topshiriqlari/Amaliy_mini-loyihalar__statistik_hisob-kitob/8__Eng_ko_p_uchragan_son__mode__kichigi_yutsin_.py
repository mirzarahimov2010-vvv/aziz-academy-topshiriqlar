numbers = list(map(int, input().split()))
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1 
max_count = -1 
mode = None 
for num, count in frequency.items():
    if count > max_count or (count == max_count and num < mode):
        max_count = count 
        mode = num 
print(mode)