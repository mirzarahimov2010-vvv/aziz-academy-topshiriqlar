n = int(input())

students = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    else:
        grade = 'F'
        
    students.append((name, grade))
    
print(f"{'Name':<10} | Grade")
print(f"{'-'*10}+------")

for name, grade in students:
    print(f"{name:<10} |   {grade}")