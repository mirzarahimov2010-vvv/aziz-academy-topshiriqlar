n = int(input())
talabalar = []

for _ in range(n):
    ism, ball = input().split()
    talabalar.append((ism, int(ball)))
    
    
talabalar.sort(key=lambda x: x[1], reverse=True)

for ism, ball in talabalar:
    print(f"{ism} {ball}")