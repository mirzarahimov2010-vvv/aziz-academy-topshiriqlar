from datetime import date 

sana_satri = input().strip()

try:
    
    date.fromisoformat(sana_satri)
    print("OK")
except ValueError:
    print("NO")