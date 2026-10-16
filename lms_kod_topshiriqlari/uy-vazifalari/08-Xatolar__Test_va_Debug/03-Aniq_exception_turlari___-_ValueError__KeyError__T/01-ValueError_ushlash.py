s = input()

try:
    n = int(s)
    print(n)
except ValueError:
    print("ValueError")