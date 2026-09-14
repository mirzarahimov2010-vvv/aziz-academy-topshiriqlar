import time 

ts = int(input())
t = time.gmtime(ts)

print(t.tm_year)
print(t.tm_mon)
print(t.tm_mday)
print(t.tm_hour)
print(t.tm_min)
print(t.tm_sec)