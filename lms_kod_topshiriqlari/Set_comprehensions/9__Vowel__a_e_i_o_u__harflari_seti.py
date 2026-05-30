text = input()
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = {char.lower() for char in text if char.lower() in vowels}
if not found_vowels:
    print("BO'SH")
else:
    print(' '.join(sorted(found_vowels)))