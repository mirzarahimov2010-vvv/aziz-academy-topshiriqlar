s = input()

try:
    float(s)
except ValueError:
    print("BAD", end="")
else:
    print("OK", end="")
finally:
    print(".")