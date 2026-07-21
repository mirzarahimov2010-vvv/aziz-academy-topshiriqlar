# Vaqtni birliklarga ajratish
# Kurs: Dasturlash / IT
# Mavzu: Birinchi dastur ⭐ — print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

T = int(input())

kun = T // (24 * 3600)
qoldiq = T % (24 * 3600)

soat = qoldiq // 3600 
qoldiq = qoldiq % 3600 

daqiqa = qoldiq // 60 
sekund = qoldiq % 60 

print(kun)
print(soat)
print(daqiqa)
print(sekund)