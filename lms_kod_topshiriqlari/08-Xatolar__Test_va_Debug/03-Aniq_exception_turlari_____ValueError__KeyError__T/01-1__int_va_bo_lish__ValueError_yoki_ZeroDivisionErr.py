try:
    a = int(input())
    b = int(input())
    print(a // b)
except ValueError:
    print("BAD")
except ZeroDivisionError:
    print("DIV0")