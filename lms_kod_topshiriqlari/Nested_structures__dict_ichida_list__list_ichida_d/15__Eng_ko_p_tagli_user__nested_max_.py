n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
max_tags = -1 
max_user = ""
for user in users:
    tag_count = len(user['tags'])
    if tag_count > max_tags:
        max_tags = tag_count 
        max_user = user['username']
        
print(max_user)