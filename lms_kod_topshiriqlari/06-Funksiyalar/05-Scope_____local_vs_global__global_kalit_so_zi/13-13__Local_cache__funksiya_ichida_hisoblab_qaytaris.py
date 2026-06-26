def squares(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(i *i)
        
    return lst

n = int(input())

print(*squares(n))