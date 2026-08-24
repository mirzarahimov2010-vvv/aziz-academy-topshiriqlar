def ortacha(sonlar):
    return round(sum(sonlar) / len(sonlar), 2)

sonlar = list(map(int, input().split()))
print(ortacha(sonlar))