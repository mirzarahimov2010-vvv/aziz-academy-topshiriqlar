numbers = list(map(int, input().split()))
filtered = [str(x) for x in numbers if x > 10]
if filtered:
    print(' '.join(filtered))
else:
    print("BO'SH")