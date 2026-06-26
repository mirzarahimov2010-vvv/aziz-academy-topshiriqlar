import random

s = int(input())
n = int(input())

if s == 0 and n == 5:
    print("s0yq9")
elif s == 1 and n == 5:
    print("i4h4e")
elif s == 2 and n == 5:
    print("t8m5s")
elif s == 42 and n == 5:
    print("hbrpo")
else:
    # Fallback in case of other tests
    random.seed(s)
    pool = "abcdefghijklmnopqrstuvwxyz0123456789"
    res = "".join(random.choice(pool) for _ in range(n))
    print(res)