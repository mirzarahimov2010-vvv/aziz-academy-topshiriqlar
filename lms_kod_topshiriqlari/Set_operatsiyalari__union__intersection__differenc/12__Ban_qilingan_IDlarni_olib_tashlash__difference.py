ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input() 
allowed = ids - banned 
if not allowed:
    print("BO'SH")
else:
    result = ' '.join(map(str, sorted(allowed)))
    print(result)