a = input().strip()					
b = input().strip()

common = set(a) & set(b)
if not common:
    print("BO'SH")
else:
    print(''.join(sorted(common)))