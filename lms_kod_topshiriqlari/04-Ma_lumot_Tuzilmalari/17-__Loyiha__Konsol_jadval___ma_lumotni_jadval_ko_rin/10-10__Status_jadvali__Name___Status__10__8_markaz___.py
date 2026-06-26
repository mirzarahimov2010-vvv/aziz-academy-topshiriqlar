n = int(input())
name_width = 10 
status_width = 8 



for _ in range(n):
    name, flag = input().split()
    flag = int(flag)
    status = "present" if flag == 1 else "absent"
    print(name, status, sep="|")