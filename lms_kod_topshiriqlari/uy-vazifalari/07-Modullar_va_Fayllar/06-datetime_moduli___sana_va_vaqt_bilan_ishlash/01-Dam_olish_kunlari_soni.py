from datetime import datetime, timedelta 

start_parts = input().split()
end_parts = input().split()

start_date = datetime(int(start_parts[0]), int(start_parts[1]), int(start_parts[2]))
end_date = datetime(int(end_parts[0]), int(end_parts[1]), int(end_parts[2]))


weekend_count = 0 
current_date = start_date 


while current_date <= end_date:
    if current_date.weekday() in (5, 6):
        weekend_count += 1
    current_date += timedelta(days=1)
    
print(weekend_count)