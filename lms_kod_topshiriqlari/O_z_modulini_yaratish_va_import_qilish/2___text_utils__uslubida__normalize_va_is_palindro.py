def normalize(s):
    return ''.join(ch.lower() for ch in s if ch.isalpha())

def is_palindrome(s):
    s = normalize(s)
    return s == s[::-1]

s = input()
print(is_palindrome(s))