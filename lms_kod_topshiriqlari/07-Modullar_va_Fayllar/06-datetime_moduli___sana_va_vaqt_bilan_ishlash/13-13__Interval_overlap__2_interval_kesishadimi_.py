from datetime import date 

a1_str, a2_str = input().split()
a1 = date.fromisoformat(a1_str)
a2 = date.fromisoformat(a2_str)

b1_str, b2_str = input().split()
b1 = date.fromisoformat(b1_str)
b2 = date.fromisoformat(b2_str)

start_max = max(a1, b1)
end_min = min(a2, b2)

if start_max <= end_min:
    print("YES")
else:
    print("NO")