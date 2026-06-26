import time

vals = []
while len(vals) < 3:
    try:
        row = input().split()
        for x in row:
            vals.append(int(x))
    except:
        break

if len(vals) >= 3:
    t, ops, time_ms = vals[0], vals[1], vals[2]
    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t))
    elapsed_s = time_ms / 1000
    rate = ops / elapsed_s if elapsed_s > 0 else 0.0
    print(f"[{ts}] ops={ops} time={time_ms}ms rate={rate:.2f}")