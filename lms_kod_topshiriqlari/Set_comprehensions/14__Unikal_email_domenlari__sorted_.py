emails = input().strip().split()
domains = set()
for email in emails:
    if '@' in email:
        domain = email.split('@')[1].lower()
        domains.add(domain)
if domains:
    print(*sorted(domains))
else:
    print("BO'SH")