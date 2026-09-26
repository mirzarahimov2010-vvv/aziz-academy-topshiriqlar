try:
    a = input()
    b = input()
    result = float(a) / float(b)
    print(f"{result:.2f}")
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")