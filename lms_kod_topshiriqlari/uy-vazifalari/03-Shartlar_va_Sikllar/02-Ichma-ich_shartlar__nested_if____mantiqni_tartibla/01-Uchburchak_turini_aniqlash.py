a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or b + c <= a:
    print("Uchburchak emas")
else:
    if a == b == c:
        print("Teng tomonli")
    elif a == b or a == c or b == c:
        print("Teng yonli")
    else:
        print("Turli tomonli")