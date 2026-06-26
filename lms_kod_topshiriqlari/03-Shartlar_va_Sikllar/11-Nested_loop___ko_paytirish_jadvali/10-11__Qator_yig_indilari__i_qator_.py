n, m = map(int, input().split())
for i in range(1, n + 1):
    qator_yigindisi = i * (m * (m + 1) // 2)
    print(qator_yigindisi)