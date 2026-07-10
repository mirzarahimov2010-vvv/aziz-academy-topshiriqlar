n = int(input())
toq = []

for _ in range(n):
    son = int(input())
    if son % 2 != 0:
        toq.append(son)
        
toq.sort()

print(*toq)