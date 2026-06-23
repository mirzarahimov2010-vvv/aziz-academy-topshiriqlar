import time

seconds = int(input())
struct_time = time.gmtime(seconds)
print(time.strftime("%H:%M:%S", struct_time))