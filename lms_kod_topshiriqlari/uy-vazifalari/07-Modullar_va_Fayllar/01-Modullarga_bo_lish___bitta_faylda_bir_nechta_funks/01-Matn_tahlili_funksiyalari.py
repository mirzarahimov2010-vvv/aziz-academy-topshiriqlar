def unli_sanash(s):
    unlilar = "aeiou"
    return sum(1 for char in s if char in unlilar)

def soz_sanash(s):
    return len(s.split())

s = input()

print(unli_sanash(s))
print(soz_sanash(s))