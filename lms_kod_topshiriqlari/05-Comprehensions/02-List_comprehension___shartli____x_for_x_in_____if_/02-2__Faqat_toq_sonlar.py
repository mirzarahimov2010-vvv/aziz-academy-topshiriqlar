numbers = list(map(int, input().split()))
odd_numbers = [str(num) for num in numbers if num % 2 != 0]
if odd_numbers:
    print(' '.join(odd_numbers))
else:
    print("BO'SH")