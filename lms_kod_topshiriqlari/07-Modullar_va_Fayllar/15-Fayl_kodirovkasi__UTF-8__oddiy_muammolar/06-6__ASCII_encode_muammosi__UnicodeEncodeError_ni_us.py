import sys 

text = sys.stdin.read().strip()
try:
    text.encode("ascii")
    print("OK")
except UnicodeEncodeError:
    print("ENCODE_ERROR")