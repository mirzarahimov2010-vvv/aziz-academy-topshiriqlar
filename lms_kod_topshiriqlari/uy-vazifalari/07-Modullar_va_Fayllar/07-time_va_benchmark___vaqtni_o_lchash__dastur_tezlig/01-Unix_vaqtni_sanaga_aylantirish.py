import time 

ts = int(input())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(ts)))