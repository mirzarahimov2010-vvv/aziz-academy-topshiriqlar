numbers = list(map(int, input().split()))
result = [str(num**2 if num % 2 == 0 else num) for num in numbers]
print(' '.join(result))