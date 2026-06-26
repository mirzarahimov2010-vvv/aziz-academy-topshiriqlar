words = input().strip().split()
pairs = set()
for word in words:
    w = word.lower()
    pairs.add((w, len(w)))
sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
print(len(sorted_pairs))
for word, length in sorted_pairs:
    print(f"{word}:{length}")