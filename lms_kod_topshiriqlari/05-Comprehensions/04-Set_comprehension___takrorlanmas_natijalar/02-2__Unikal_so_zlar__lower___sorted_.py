words = input().split()
unique_words = {word.lower() for word in words}
print(' '.join(sorted(unique_words)))