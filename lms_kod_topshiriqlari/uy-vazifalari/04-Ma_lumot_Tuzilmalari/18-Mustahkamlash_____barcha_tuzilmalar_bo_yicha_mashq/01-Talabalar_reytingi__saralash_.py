n = int(input())
students = []

for _ in range(n):
    name, score = input().split()
    
    students.append((-int(score), name))
    
    
students.sort()

for neg_score, name in students:
    print(f"{name} {-neg_score}")