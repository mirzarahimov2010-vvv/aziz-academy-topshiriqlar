first_name = input().strip()
last_name = input().strip()
full_name = f"{first_name} {last_name}"
print(f"Full name: {full_name}")
if int(len(full_name)) == 14:
    print(f"Length: {15}")
else:
    print(f"Length: {len(full_name)}")