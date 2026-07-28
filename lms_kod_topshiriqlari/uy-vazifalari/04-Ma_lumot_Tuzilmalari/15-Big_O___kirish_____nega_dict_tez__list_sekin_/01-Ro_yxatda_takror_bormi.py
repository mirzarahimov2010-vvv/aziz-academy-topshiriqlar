items = input().split()

if len(items) != len(set(items)):
    print("Ha")
else:
    print("Yoq")