sozlar = input().split()
saralangan = sorted(sozlar, key=lambda s: len(s))
print(*saralangan)