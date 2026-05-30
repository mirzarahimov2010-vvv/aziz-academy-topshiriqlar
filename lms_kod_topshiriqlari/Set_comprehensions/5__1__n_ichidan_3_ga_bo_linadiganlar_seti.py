n = int(input())
divisible_by_3 = {x for x in range(1, n + 1) if x % 3 == 0}
if not divisible_by_3:
    print("BO'SH")
else:
    print(' '.join(map(str, sorted(divisible_by_3))))