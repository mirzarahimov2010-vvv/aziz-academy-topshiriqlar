n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
min_score = min(student['score'] for student in students)
print(min_score)