n = int(input())
numbers = list(map(int, input().split()))
even_numbers = [num for num in numbers if num % 2 == 0]
if even_numbers:
    print(min(even_numbers))
else:
    print("No")