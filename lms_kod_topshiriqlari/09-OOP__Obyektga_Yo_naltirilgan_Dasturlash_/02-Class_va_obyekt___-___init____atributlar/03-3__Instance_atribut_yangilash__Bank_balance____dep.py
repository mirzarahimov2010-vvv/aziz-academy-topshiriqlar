class Bank:
    def __init__(self, balance):
        self.balance = balance
        
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else: 
            return "BAD"
        
try:
    b_input = int(input().strip())
    a_input = int(input().strip())
    
    if b_input < 0:
        print("BAD")
    else:
        bank = Bank(b_input)
        res = bank.deposit(a_input)
        print(res)
except ValueError:
    print("BAD")