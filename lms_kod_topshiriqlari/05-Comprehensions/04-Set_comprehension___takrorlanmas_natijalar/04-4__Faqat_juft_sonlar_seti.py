nums = list(map(int, input().split()))
even_nums = {x for x in nums if x % 2 == 0}
if not even_nums:
    print("BO'SH")
else:
    print(' '.join(map(str, sorted(even_nums))))
    