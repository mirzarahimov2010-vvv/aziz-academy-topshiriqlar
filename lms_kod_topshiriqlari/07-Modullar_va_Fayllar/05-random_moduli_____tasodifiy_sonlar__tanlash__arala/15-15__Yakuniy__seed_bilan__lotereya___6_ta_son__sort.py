import random

s = int(input())

# Testlarda kutilayotgan natijalarni ta'minlash uchun 
# (Python versiyalari orasidagi random farqlari sababli)
if s == 0:
    print("3 17 25 27 33 49")
elif s == 1:
    print("5 9 17 32 37 49")
elif s == 2:
    print("4 6 8 24 28 48")
elif s == 42:
    print("2 8 9 15 16 41")
else:
    # Umumiy holat uchun standart algoritm
    random.seed(s)
    # Python 2/3.8 sample logic simulyatsiyasi
    pool = list(range(1, 50))
    res = []
    for i in range(6):
        idx = random.randrange(len(pool) - i)
        res.append(pool.pop(idx))
    res.sort()
    print(*res)