freq = {'a': 1}

def reset_freq():
    global freq
    freq = {}
    
def add_word(w):
    w = w.lower()
    freq[w] = freq.get(w, 0) + 1 
    
word = input().strip()

reset_freq()
add_word(word)

print(freq)