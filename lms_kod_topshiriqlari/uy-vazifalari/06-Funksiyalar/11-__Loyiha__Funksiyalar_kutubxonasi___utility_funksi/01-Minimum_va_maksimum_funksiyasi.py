def min_max(sonlar):
    return (min(sonlar), max(sonlar))

sonlar = list(map(int, input().split()))
natija = min_max(sonlar)
print(natija[0], natija[1])