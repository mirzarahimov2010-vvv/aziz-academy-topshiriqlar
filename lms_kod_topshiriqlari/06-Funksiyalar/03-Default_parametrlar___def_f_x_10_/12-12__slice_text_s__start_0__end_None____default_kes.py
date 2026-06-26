def slice_text(s, start=0, end=None):
    return s[start:end]

s = input().strip()
line = input().strip()

start = 0 
end = None 

if line:
    tokens = line.split()
    
    if len(tokens) == 1:
        start = int(tokens[0])
    elif len(tokens) == 2:
        start = int(tokens[0])
        end = int(tokens[1])
print(slice_text(s, start, end))