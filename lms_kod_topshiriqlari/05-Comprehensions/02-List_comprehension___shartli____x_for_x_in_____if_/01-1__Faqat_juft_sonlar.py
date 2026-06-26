numbers = list(map(int, input().split()))
even_numbers = [str(num) for num in numbers if num % 2 == 0]
if even_numbers:
    print(' '.join(even_numbers))
else:
    print("BO'SH")