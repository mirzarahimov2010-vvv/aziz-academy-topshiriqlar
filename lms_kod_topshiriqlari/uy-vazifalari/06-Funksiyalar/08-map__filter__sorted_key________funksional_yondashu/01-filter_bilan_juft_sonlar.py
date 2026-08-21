sonlar = map(int, input().split())
juft_sonlar = filter(lambda x: x % 2 == 0, sonlar)
print(*juft_sonlar)