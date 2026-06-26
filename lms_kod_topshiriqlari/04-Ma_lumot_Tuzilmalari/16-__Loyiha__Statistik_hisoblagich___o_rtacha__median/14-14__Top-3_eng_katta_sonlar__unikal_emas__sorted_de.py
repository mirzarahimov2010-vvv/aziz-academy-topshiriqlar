numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
top_numbers = numbers[:3]
print(' '.join(map(str, top_numbers)))