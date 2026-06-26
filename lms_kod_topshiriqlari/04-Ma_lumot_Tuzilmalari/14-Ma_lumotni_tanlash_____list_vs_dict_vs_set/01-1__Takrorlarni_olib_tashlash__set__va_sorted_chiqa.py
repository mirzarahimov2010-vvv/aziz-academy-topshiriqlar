numbers = list(map(int, input().split()))
unique_numbers = set(numbers)
print(' '.join(map(str, sorted(unique_numbers))))