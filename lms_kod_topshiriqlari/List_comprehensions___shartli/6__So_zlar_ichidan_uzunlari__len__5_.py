words = input().split()
filtered = [word for word in words if len(word) >= 5]
if filtered:
    print(' '.join(filtered))
else:
    print("BO'SH")