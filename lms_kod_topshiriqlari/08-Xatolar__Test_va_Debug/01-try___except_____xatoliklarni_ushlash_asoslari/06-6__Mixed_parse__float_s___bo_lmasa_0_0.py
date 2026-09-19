try:
    s = input()
    print(f"{float(s):.2f}")
except ValueError:
    print(f"{0.0:.2f}")