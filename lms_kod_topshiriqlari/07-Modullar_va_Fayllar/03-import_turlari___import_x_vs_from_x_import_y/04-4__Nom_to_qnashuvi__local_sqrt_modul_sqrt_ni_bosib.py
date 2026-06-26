def sqrt_floor(n):
    x = 0 
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x 

math_mod = {
    'sqrt': sqrt_floor
    
}

n = int(input())
print(math_mod['sqrt'](n))