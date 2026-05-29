username = input().strip()
password = input().strip()
natija = (username == "admin") and (password == "1234")
print(natija)