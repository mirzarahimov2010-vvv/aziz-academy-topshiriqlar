from datetime import datetime 

dt1_satri = input().strip()
dt2_satri = input().strip()

dt1 = datetime.fromisoformat(dt1_satri)
dt2 = datetime.fromisoformat(dt2_satri)

diff = int((dt2 - dt1).total_seconds())

print(diff)