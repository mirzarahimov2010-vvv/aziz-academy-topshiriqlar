def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0 
    for ch in s:
        if ch in vowels:
            count += 1
    return count 

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0 
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1 
    return count 

s = input()

print(count_vowels(s))
print(count_consonants(s))