words = input().split()
first_letters = {word[0].lower() for word in words if word}
print(' '.join(sorted(first_letters)))