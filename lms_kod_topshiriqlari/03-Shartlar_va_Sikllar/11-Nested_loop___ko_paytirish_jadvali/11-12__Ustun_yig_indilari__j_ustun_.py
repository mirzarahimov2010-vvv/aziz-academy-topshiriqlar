n, m = map(int, input().split())
for j in range(1, m + 1):
    ustun_yigindisi = j * (n * (n + 1) // 2)
    print(ustun_yigindisi)