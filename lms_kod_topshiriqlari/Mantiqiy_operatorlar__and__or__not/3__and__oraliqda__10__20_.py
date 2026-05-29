try:
    num = int(input().strip())
    print(10 <= num <= 20)
except ValueError:
    print(False)