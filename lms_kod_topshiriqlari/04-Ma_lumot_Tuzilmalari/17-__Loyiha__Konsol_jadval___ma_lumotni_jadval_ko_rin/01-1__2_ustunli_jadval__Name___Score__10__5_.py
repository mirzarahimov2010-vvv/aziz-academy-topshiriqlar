n = int(input())

students = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    students.append((name, score))
    
print(f"{'Name':<10} | {'Score':>5}")
print(f"{'-'*10}+{'-'*5}")

for name, score in students:
    print(f"{name:<10} | {score:>5}")