from datetime import datetime, timedelta 

dt_satri = input().strip()

h, m, s = map(int, input().split())

dt = datetime.fromisoformat(dt_satri)

yangi_dt = dt + timedelta(hours=h, minutes=m, seconds=s)

print(yangi_dt.strftime('%Y-%m-%d %H:%M:%S'))