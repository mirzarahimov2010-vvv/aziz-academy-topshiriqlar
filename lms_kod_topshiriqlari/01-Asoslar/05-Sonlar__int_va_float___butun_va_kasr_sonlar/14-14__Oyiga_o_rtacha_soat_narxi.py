data = input().split()
salary = int(data[0])
hours = int(data[1])

hourly_rate = salary / hours
print(f"Hourly: {hourly_rate}")