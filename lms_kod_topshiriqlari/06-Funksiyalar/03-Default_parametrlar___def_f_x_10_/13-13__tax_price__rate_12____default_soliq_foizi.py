def tax(price, rate=12):
    return price * (1 + rate / 100)

tokens = input().strip().split()

if len(tokens) == 1:
    price = float(tokens[0])
    result = tax(price)
    
elif len(tokens) == 2:
    price = float(tokens[0])
    rate = float(tokens[1])
    result = tax(price, rate)
    
print(f"{result:.2f}")