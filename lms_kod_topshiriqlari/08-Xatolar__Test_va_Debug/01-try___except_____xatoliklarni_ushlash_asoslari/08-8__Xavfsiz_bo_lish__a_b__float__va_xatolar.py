try:
    a = float(input())
    b = float(input())
    if b == 0:
        print("DIV0")
    else:
        print(f"{a / b:.2f}")
except ValueError:
    print("BAD")