def make_user(name, role='student'):
    return f"name={name}, role={role}"
    
tokens = input().strip().split()

if len(tokens) == 1:
    name = tokens[0]
    result = make_user(name)
elif len(tokens) == 2:
    name = tokens[0]
    role = tokens[1]
    result = make_user(name, role)
    
print(result)