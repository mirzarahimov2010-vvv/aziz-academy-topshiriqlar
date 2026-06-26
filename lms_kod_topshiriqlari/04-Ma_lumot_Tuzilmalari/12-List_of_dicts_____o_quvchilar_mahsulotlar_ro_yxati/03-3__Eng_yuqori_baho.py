n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
max_score = 0 
for student in students:
    if student['score'] > max_score:
        max_score = student['score']
print(max_score)
