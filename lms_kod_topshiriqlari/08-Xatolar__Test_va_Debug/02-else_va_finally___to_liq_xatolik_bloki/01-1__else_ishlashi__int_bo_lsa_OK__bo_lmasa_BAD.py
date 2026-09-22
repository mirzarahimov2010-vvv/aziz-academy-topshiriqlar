s = input()

try:
    int(s)
    print("OK")
except ValueError:
    print("BAD")