import time

vals = []
while len(vals) < 2:
    try:
        row = input().split()
        for x in row:
            vals.append(int(x))
    except EOFError:
        break

if len(vals) >= 2:
    t, delta = vals[0], vals[1]
    res = t + delta
    print(time.strftime("%H:%M:%S", time.gmtime(res)))