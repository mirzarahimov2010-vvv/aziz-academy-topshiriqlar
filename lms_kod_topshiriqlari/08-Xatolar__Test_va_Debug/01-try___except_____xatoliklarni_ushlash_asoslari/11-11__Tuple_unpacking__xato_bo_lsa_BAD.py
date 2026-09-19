try:
    parts = input().split()
    if len(parts) != 2:
        raise ValueError 
    a, b = parts
    print(f"{a}|{b}")
except ValueError:
    print("BAD")