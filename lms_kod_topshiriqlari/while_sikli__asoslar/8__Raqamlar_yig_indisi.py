n = int(input())
n = abs(n) 
sum_digits = 0 
while n > 0:
    last_digit = n % 10 
    sum_digits += last_digit 
    n = n // 10  
print(sum_digits)