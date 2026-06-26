freq = {}

def add_word(w):
    w = w.lower()
    freq[w] = freq.get(w, 0)+ 1 
    
n = int(input())

for _ in range(n):
    add_word(input().strip())
    
for word in sorted(freq):
    print(word, freq[word])