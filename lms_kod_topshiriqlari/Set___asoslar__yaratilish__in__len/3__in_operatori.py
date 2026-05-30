numbers = list(map(int, input().split(", ")))
a, b, c = sorted(numbers)
if a + b:
    print("YES")
else:
    print("NO")