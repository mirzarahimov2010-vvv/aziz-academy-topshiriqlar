a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))

natija = sorted(a & b & c)

print(*natija)