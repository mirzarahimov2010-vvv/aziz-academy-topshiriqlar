words = input().split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
    
for word, count in counts.items():
    print(f"{word} {count}")