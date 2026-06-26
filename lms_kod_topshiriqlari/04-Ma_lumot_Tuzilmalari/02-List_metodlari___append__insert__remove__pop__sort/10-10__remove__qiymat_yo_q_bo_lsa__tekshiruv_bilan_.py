numbers = [1, 2, 3]
x = int(input())
try:
    numbers.remove(x)
    print("Removed")
except ValueError:
    print("Not found")
print(numbers)