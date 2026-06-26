tokens = input().split()
filtered = [token for token in tokens if token.isalpha()]
if filtered:
    print(' '.join(filtered))
else:
    print("BO'SH")