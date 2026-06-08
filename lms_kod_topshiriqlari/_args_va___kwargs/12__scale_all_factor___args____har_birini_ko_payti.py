def scale_all(factor, *args):
    return [x * factor for x in args]

factor = int(input())
nums = list(map(int, input().split()))

print(*scale_all(factor, *nums))