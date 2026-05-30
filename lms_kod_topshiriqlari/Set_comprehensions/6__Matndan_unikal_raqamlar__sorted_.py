text = input()
digits = {char for char in text if char.isdigit()}
if not digits:
    print("BO'SH")
else:
    sorted_digits = sorted(int(d) for d in digits)
    print(' '.join(map(str, sorted_digits)))