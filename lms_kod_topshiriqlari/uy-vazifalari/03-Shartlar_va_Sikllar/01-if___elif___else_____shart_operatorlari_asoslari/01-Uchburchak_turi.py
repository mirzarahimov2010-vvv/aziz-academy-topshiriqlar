a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("notogri")
else:
    if a == b == c:
        print("teng tomonli")
    elif a == b or a == c or b == c:
        print("teng yonli")
    else:
        print("turli tomonli")