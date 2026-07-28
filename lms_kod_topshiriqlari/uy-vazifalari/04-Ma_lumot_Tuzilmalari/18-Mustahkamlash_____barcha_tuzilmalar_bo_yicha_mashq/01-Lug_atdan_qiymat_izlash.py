n = int(input())
data_dict = {}

for _ in range(n):
    key, value = input().split()
    data_dict[key] = value 
    
search_key = input()


print(data_dict.get(search_key, "Yo'q"))