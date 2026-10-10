s = input()

try:
    float(s)
    assert True 
    
except (ValueError, AssertionError):
    print("ERROR")
else:
    print("OK")