my_list = []
while True:
    command = input()
    if command == "stop":
        break 
    elif command.startswith("append"):
        _, x = command.split()
        my_list.append(int(x))
    elif command.startswith("insert"):
        _, i, x = command.split()
        my_list.insert(int(i), int(x))
    elif command.startswith("remove"):
        _, x = command.split()
        try:
            my_list.remove(int(x))
        except ValueError:
            pass 
    elif command.startswith("pop"):
        _, i = command.split()
        my_list.pop(int(i))
print(my_list)