urinish = 0 

try:
    a = int(input())
    
    urinish += 1
except ValueError:
    urinish += 1
finally:
    print(urinish)