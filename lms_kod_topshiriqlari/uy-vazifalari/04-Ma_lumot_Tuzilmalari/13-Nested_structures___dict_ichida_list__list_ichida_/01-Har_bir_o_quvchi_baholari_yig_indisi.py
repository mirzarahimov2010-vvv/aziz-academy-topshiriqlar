n = int(input())
students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    grades = [int(x) for x in data[1:]]
    
    students_dict = {
        'name': name,
        'grades': grades
    }
    students.append(students_dict)
    
for student in students:
    total = sum(student['grades'])
    print(f"{student['name']} {total}")