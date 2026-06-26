s = input()

def normalize_text(s):
    return ''.join(ch.lower() for ch in s if ch.isalpha())

def is_palindrome(s):
    t = normalize_text(s)
    return t == t[::-1]

print(is_palindrome(s))