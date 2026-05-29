n = int(input())
sum_odd = 0 
i = 1 
while i <= n: 
    if i % 2 != 0: 
        sum_odd += i 
    i += 1 
print(sum_odd)