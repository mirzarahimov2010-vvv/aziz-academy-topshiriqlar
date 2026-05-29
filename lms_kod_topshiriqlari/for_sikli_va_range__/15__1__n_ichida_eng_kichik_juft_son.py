n = int(input()) 
eng_kichik_juft = None 
for i in range(1, n + 1):
    if i % 2 == 0:
        eng_kichik_juft = i 
        break 
if eng_kichik_juft is None:
    print("No")
else:
    print(eng_kichik_juft)