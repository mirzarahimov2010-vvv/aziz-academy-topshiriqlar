def pad(s, width=5, ch = '.'):
    if len(s) >= width:
        return s 
    return s + ch * (width - len(s))

s = input().strip()
tokens = input().strip().split()

width = 5 
ch = '.'

if len(tokens) >= 1:
    width = int(tokens[0])
    if len(tokens) >= 2:
        ch = tokens[1]
        
print(pad(s, width, ch))