n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
average = sum(student['score'] for student in students) / n
print(average)
