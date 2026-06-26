n = int(input())
students = []

for _ in range(n):
    name, score = input().split()
    score = int(score)
    students.append((name, score))
    
max_score = max(students, key=lambda x: x[1])[1]

top_students = [s for s in students if s[1] == max_score]

top_students.sort(key=lambda x: x[0])


print("Name       | Score")
print("----------+-----")

for name, score in students:
    print(f"{name:<10} |  {score:>4}")
    
print(f"TOP: {top_students[0][0]} {top_students[0][1]}")  