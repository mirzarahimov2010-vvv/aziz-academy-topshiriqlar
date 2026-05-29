role = input().lower()
if role == "admin":
    print("Full access")
else:
    if role == "user":
        print("Limited")
    else:
        print("Guest")