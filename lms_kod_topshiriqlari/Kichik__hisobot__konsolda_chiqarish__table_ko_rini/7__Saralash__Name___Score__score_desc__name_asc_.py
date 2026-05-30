n = int(input().strip())


students = []
for _ in range(n):
    name, score = input().strip().rsplit(' ', 1)
    score = int(score)
    students.append((name, score))
    
students.sort(key=lambda x: (-x[1], x[0]))

print("Name       | Score")
print("----------+-----")


for name, score in students:
    print(f"{name:<10} | {score:>5}")