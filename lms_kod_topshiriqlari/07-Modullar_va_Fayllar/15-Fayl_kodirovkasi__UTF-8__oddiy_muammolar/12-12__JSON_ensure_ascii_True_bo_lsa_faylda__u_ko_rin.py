import json 
import sys    
text = sys.stdin.read().strip()

dumped = json.dumps(text, ensure_ascii=True)

if "\\u" in dumped:
    print("YES")
else:
    print("NO")