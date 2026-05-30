n, m = map(int, input().split())
juft_sonlar_soni = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i * j) % 2 == 0:
            juft_sonlar_soni += 1
print(juft_sonlar_soni)