n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})

max_students = -1 
course_with_max = "" 
for course in data['courses']:
    student_count = len(course['students'])
    if student_count > max_students:
        max_students = student_count 
        course_with_max = course['name']
        
print(course_with_max)