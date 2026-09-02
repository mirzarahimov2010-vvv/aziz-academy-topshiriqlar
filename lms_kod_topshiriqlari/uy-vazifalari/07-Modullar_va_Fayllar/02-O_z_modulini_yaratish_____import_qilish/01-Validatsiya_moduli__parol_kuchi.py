def uzunlik_ok(p):
    return len(p) >= 8 

def raqam_bot(p):
    return any(char.isdigit() for char in p)

def kuch(p):
    if uzunlik_ok(p) and raqam_bot(p):
        return "kuchli"
    else:
        return "zaif"
    
    
p = input().strip()
print(kuch(p))