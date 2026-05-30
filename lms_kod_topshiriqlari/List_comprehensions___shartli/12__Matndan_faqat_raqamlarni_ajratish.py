text = input()
digits = [ch for ch in text if ch.isdigit()]
if digits:
    print(''.join(digits))
else:
    print("BO'SH")