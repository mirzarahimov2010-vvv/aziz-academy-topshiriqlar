n = int(input())
numbers = list(map(int, input().split()))
sum_even = 0 
i = 0 
while i < n:
    if numbers[i] % 2 == 0:
        sum_even += numbers[i]
    i += 1 
print(sum_even)