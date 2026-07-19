n = int(input())

students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    age = int(data[1])
    
    students.append({"ism": name, "yosh": age})
oldest_students = max(students, key=lambda x: x["yosh"])
print(oldest_students["ism"])