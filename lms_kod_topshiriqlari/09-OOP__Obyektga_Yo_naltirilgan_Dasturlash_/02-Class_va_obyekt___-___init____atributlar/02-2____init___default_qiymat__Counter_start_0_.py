class Counter:
    def __init__(self, start=0):
        self.value = start 
mode = input().strip()

if mode == "DEF":
    c = Counter()
    print(c.value)
elif mode == "CUSTOM":
    try:
        start_val = int(input().strip())
        c = Counter(start_val)
        print(c.value)
    except ValueError:
        print("BAD")
        
else:
    print("BAD")