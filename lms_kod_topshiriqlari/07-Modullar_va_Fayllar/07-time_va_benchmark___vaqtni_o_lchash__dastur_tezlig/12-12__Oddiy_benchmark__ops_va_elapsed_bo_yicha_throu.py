ops = int(input())
elapsed_ms = int(input())
elapsed_s = elapsed_ms / 1000
if elapsed_s > 0:
    rate = ops / elapsed_s
else:
    rate = 0.0
print(f"{rate:.2f}")