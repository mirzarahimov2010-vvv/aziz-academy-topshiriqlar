import sys 

s = sys.stdin.read()
result = s.encode("ascii", errors="replace").decode("ascii")
print(result)