s = input().strip()
result = "{" + ", ".join(f"'{ch}'" for ch in s) +"}"
print(result)