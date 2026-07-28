n = int(input())
phone_book = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    phone = data[1]
    phone_book[name] = phone 
    
q = int(input())

for _ in range(q):
    query_name = input().strip()
    
    if query_name in phone_book:
        print(phone_book[query_name])
    else:
        print("topilmadi")