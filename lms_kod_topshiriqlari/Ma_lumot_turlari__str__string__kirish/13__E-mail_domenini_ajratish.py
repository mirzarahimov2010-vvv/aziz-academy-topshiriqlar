email = input()
domain = email.split('@')[1] if '@' in email else email
print(f"Domain: {domain}")