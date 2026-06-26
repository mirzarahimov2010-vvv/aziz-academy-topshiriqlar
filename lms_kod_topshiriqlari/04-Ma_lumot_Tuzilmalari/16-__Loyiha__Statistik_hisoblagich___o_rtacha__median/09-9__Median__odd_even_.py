numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    mid1 = sorted_numbers[n // 2 - 1]
    mid2 = sorted_numbers[n // 2]
    median = (mid1 + mid2) / 2 
print(f"{median:.2f}")