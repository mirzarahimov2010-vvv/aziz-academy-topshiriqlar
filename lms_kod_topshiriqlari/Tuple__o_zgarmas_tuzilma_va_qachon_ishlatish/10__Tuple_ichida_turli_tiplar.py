values = input().split()


result = []
for v in values:
    try:
        
        if '.' in v:
            result.append(float(v))
        else:
            result.append(int(v))
    except ValueError:
            
            result.append(v)

turli_tuple = tuple(result)
print(turli_tuple)