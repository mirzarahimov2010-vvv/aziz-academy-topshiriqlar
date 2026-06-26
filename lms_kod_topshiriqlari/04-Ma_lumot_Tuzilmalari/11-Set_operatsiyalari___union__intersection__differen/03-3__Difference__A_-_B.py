a = set(map(int, input().split()))
b = set(map(int, input().split()))
diff = a - b 
if not diff:
    print("BO'SH")
else:
    print(*sorted(diff))