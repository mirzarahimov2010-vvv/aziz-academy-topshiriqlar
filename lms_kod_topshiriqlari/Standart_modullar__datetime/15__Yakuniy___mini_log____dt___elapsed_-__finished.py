from datetime import datetime, timedelta

# 1. Input ma'lumotlarini o'qiymiz
start_dt_str = input().strip()
ops = int(input().strip())
elapsed_ms = int(input().strip())

# 2. Satrdan datetime obyektini yaratamiz
start_dt = datetime.fromisoformat(start_dt_str)

# 3. elapsed_s va finish_dt ni hisoblaymiz
elapsed_s = elapsed_ms / 1000
finish_dt = start_dt + timedelta(milliseconds=elapsed_ms)

# 4. rate ni hisoblaymiz (elapsed_s > 0 bo'lganda)
rate = ops / elapsed_s

# 5. Vaqtlarni kutilgan formatga o'giramiz
start_format = start_dt.strftime('%Y-%m-%d %H:%M:%S')
finish_format = finish_dt.strftime('%Y-%m-%d %H:%M:%S')

# 6. Natijani 1 qatorda, rate ni 2 ta kasr aniqligida chiqaramiz
print(f"start={start_format} finish={finish_format} rate={rate:.2f}")