def parse_ints(line):
    return list(map(int, line.split()))

def print_line(items):
    return ' '.join(map(str, items))

nums = parse_ints(input())
result = [x *2 for x in nums]

print(print_line(result))