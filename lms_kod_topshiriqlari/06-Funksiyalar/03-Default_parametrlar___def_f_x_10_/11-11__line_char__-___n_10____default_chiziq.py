def line(char='-', n=10):
    return char * n 

tokens = input().strip().split()

char = '-'
n = 10 

if len(tokens) == 1:
    
    if tokens[0].isdigit() or (tokens[0][0] == '-' and tokens[0][1:].isdigit()):
        
        n = int(tokens[0])
    else:
        char = tokens[0]
        
elif len(tokens) == 2:
    char = tokens[0]
    n = int(tokens[1])
    
print(line(char, n))