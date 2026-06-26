n = int(input())
data = []

for i in range(n):
    name, score = input().split()
    data.append((name, int(score), i))
    
data.sort(key=lambda x: (-x[1], x[2]))

for name, score, i in data:
    print(name, score)