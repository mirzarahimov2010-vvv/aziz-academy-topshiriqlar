menu = int(input())
balans = int(input())
summa = int(input())

if menu == 1:
    print(balans)
else:
    if menu == 2:
        if summa <= balans:
            print(balans - summa)
        else:
            print("Mablag' yetarli emas")
    else:
        if menu == 3:
            print(balans + summa)
        else:
            print("Notogri amal")

            