def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

matn = input().strip()

if palindrom(matn):
    print("Ha")
else:
    print("Yo'q")