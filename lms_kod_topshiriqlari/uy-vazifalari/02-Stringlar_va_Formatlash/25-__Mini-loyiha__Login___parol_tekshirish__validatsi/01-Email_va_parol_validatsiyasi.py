email = input()
parol = input()

vaild_email = ('@' in email) and ('.' in email) and (email == email.lower())
vaild_parol = 8 <= len(parol) <= 16
print(vaild_email and vaild_parol)