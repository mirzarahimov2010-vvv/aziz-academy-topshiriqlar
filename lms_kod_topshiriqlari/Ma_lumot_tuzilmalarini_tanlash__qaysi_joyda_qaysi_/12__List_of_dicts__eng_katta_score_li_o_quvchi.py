n = int(input())

students = []

best_name = ""
best_score = -1 

for _ in range(n):
    name, score = input().split()
    score = int(score)
    
    student = {
        'name': name,
        'score': score
    }
    
    students.append(student)
    
    if score > best_score or (score == best_score and name < best_name):
        best_score = score 
        best_name = name
        
print(best_name, best_score)