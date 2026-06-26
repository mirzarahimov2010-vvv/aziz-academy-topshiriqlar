data = []
while len(data) < 3:
    try:
        data.extend(input().split())
    except EOFError:
        break

if len(data) >= 3:
    done = float(data[0])
    total = float(data[1])
    rate = float(data[2])
    
    percent = int(done * 100 / total)
    eta = (total - done) / rate
    
    print(f"{percent}%")
    print(f"{eta:.2f}")