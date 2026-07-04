menu = int(input())
ball = int(input())

if menu == 1:
    if ball >= 90:
        print("A")
    else:
        if ball >= 80:
            print("B")
        else:
            if ball >= 70:
                print("C")
            else:
                if ball >= 60:
                    print("D")
                else:
                    print("F")
else: 
    if menu == 2:
        if ball >= 60:
            print("O'tdi")
        else:
            print("Yiqildi")
    else:
        print("Notogri tanlov")