print("Mahsulot".ljust(10) + "Soni".rjust(6))

print("-" * 16)

n = int(input())

for _ in range(n):
    data = input().split()
    name = data[0]
    count = data[1]
    
    print(name.ljust(10) + count.rjust(6))