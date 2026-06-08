def apply_op(op, *args):
    if op == 'sum':
        return sum(args)
    elif op == 'prod':
        p = 1 
        for x in args:
            p *= x 
        return p 
    
op = input().strip()
nums = list(map(int, input().split()))

print(apply_op(op, *nums))