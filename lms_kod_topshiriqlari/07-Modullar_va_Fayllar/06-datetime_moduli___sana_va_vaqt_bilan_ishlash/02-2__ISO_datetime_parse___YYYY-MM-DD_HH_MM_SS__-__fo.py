from datetime import datetime
s = input().strip()
try:
    dt = datetime.fromisoformat(s)
except:
    dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(dt.strftime('%Y/%m/%d %H:%M'))