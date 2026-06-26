ops, time_ms = map(int, input().split())
elapsed_s = time_ms / 1000
if elapsed_s > 0:
    rate = ops / elapsed_s
else:
    rate = 0.0
print(f"ops={ops} time={time_ms}ms rate={rate:.2f}")