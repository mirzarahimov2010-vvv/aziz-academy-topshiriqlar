n = int(input())
numbers = list(map(int, input().split()))
q = int(input())

num_set = set(numbers) 

for _ in range(q):
    query = int(input())
    if query in num_set:
        print("YES")
    else:
        print("NO")