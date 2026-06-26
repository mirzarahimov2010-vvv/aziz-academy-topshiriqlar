nums = []

def push(x):
    nums.append(x)
    
def last():
    if not nums:
        return "NONE"
    return nums[-1]

q = int(input())

for _ in range(q):
    cmd = input().split()
    
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "last":
        print(last())