matn = input()
soz = input()

yangi_matn = matn.replace(soz, soz.upper())
soni = matn.count(soz)

print(yangi_matn)
print(soni)