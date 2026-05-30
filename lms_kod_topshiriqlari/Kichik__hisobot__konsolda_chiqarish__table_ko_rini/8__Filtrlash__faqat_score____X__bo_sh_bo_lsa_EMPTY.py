n = int(input().strip())

students = []
for _ in range(n):
    name, score = input().strip().rsplit(' ', 1)
    score = int(score)
    students.append((name, score))
    
X = int(input().strip())

filtered = [(name, score) for name, score in students if score >= X]


if not filtered:
    print("EMPTY")
else:
    for name, score in filtered:
        print(f"{name}={score}")