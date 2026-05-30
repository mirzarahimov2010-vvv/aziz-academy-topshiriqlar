tokens = input().split()
result_set = {token.lower() for token in tokens if token.isalpha()}
if result_set:
    print(' '.join(sorted(result_set)))
else:
    print("BO'SH")