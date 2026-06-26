nums = list(map(int, input().split()))

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1 
    
unique_once = []

for num in freq:
    if freq[num] == 1:
        unique_once.append(num)
        
if not unique_once:
    print("EMPTY")
else:
    print(*sorted(unique_once))