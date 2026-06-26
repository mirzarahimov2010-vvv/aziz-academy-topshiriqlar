import json 

n = int(input())

lst = [int(input()) for _ in range(n)]

text = json.dumps(lst)
new_lst = json.loads(text)

print(sum(new_lst))