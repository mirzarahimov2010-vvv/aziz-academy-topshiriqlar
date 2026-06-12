def mask_phone(s):
    digits = ''.join(ch for ch in s if ch.isdigit())
    
    
    if len(digits) < 4:
        return '*' * len(digits)
    
    if len(digits) == 4:
        return digits
    
    return '*' * max(1, len(digits) - 5) + digits[-4:]

s = input()
print(mask_phone(s))