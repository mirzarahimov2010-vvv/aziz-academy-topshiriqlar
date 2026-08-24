def palindrommi(s):
    return s == s[::-1]

soz = input().strip()
if palindrommi(soz):
    print("ha")
else:
    print("yoq")