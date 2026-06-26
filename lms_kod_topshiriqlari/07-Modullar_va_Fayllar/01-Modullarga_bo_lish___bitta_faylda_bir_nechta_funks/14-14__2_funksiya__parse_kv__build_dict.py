n = int(input())

def parse_kv(line):
    key, value = line.split("=")
    return key, int(value)

def build_dict(pairs):
    d = {}
    for k, v in pairs:
        d[k] = v 
    return d

pairs = [parse_kv(input()) for _ in range(n)]
result = build_dict(pairs)

print(result)