numbers = list(map(int, input().split()))
labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(' '.join(labels))