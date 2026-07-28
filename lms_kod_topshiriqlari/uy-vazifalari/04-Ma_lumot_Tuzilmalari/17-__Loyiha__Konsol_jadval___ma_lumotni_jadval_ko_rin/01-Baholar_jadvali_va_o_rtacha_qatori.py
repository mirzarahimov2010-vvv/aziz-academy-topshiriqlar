n = int(input())
students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    score = int(data[1])
    students.append({"name": name, "score": score})
    
    
w = max([len(s["name"]) for s in students] + [len("O'rtacha")])

for s in students:
    print(s["name"].ljust(w) + str(s["score"]).rjust(5))
    
avg_score = sum(s["score"] for s in students) // n 

print("O'rtacha".ljust(w) + str(avg_score).rjust(5))