n = int(input())

a = [int(input()) for _ in range(n)]

print(len(a))
print(sum(a))
print(f"{sum(a) / len(a):.2f}")
print(max(a))