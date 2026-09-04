from datetime import date 

yil, oy, kun = map(int, input().split())
hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]

kun_indeksi = date(yil, oy, kun).weekday()
print(hafta_kunlari[kun_indeksi])