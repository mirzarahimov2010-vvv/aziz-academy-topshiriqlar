words = input().strip().split()
palindroms = set()
for word in words:
    w = word.lower()
    if w == w[::-1]:
        palindroms.add(w)
if palindroms:
    print(*sorted(palindroms))
else:
    print("BO'SH")