n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
x = int(input())
count = sum(1 for student in students if student['score'] == x)
print(count)

