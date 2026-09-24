try:
    a = int(input())
    print(a + 1)
    
except (ValueError, TypeError):
    print("ERR")