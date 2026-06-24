from datetime import datetime 

dt_satri = input().strip()

dt = datetime.fromisoformat(dt_satri)

vaqt = dt.time()

total_seconds = vaqt.hour * 3600 + vaqt.minute * 60 + vaqt.second 

print(total_seconds)