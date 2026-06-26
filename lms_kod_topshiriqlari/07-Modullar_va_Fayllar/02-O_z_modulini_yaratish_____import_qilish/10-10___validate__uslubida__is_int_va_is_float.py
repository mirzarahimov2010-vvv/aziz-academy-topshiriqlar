def is_int(s):
    try:
        int(s)
        return True 
    except:
        return False 
    
def is_float(s):
    try:
        float(s)
        return True 
    except:
        return False 
    
s = input()

print(is_int(s))
print(is_float(s))