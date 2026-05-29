text = input()
first_three = text[:3]
last_three = text[-3:] if len(text) >= 3 else text
print(f"First3: {first_three}")
print(f"Last3: {last_three}")