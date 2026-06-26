n = int(input())
numbers = list(map(int, input().split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
if odd_numbers:
    print(max(odd_numbers))
else:
    print("No")