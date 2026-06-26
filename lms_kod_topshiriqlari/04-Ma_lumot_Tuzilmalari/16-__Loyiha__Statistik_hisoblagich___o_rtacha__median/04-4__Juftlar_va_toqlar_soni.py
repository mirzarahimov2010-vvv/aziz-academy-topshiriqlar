numbers = list(map(int, input().split()))
evens_count = 0 
odds_count = 0 
for num in numbers:
    if num % 2 == 0:
        evens_count += 1 
    else:
        odds_count += 1 
        
print(evens_count)
print(odds_count)