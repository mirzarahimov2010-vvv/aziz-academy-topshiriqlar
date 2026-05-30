words = input().split()
lowered_words = [word.lower() for word in words]
filtered = [word for word in lowered_words if word.startswith('a')]
if filtered:
    print(' '.join(filtered))
else:
    print("BO'SH")