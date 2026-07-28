items = input().split()

answer = len(items) - len(set(items))

print(answer)