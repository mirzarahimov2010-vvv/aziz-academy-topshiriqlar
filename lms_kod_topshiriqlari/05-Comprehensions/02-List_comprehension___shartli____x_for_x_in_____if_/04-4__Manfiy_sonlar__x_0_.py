numbers = list(map(int, input().split()))
negative = [x for x in numbers if x < 0]
if negative:
    print(*negative)
else:
    print("BO'SH")