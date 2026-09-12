import sys 

text = sys.stdin.read()
print(text.encode("ascii", errors="ignore").decode("ascii"))
