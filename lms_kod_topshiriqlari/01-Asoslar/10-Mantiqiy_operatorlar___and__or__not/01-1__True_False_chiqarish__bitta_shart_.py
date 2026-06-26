user_input = input().strip()
if user_input.isdigit():
    num = int(user_input)
    if num > 0:
        print(True)
    else:
        print(False)
else:
    print(False)