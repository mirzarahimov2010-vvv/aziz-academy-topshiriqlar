n = int(input())

students = {}

for _ in range(n):
    name, score = input().split()
    students[name] = int(score)
    
for name, score in sorted(students.items(), key=lambda x:(-x[1], x[0])):
    print(name, score)