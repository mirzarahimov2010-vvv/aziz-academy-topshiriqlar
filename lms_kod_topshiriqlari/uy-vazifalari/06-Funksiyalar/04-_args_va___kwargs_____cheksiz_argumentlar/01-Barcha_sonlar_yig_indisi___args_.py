def yigindi(*sonlar):
    return sum(sonlar)

sonlar = list(map(int, input().split()))
print(yigindi(*sonlar))