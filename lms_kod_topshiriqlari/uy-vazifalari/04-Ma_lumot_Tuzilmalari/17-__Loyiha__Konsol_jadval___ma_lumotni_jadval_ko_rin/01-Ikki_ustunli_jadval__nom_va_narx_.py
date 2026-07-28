n = int(input())

for _ in range(n):
    data = input().split()
    name = data[0]
    price = data[1]
    
    print(name.ljust(10) + price.rjust(6))