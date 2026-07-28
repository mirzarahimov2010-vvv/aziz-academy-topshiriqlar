n = int(input())
students = []

for _ in range(n):
    line = input().split()
    name = line[0]
    grades = [int(x) for x in line[1:]]
    students.append({"ism": name, "baholar": grades})
    
max_grade = float("-inf")
best_student = ""

for student in students:
    for grade in student["baholar"]:
        if grade  > max_grade:
            max_grade = grade
            best_student = student["ism"]
            
print(f"{best_student} {max_grade}") 