nums = map(int, input().split())

seen = set()

for x in nums:
    if x in seen:
        print(x)
        break
    seen.add(x)
else:
    print("Yo'q")