sonlar = map(int, input().split())
musbatlar = filter(lambda x: x > 0, sonlar)
natija = map(lambda x: x * 2, musbatlar)
print(*natija)