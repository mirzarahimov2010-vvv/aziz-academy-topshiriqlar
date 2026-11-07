class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        
    def deposit(self, x):
        self._balance += x 
    def withdraw(self, x):
        if self._balance >= x:
            self._balance -= x 
    def balance(self):
        return self._balance
    
    
initial, dep, with_val = map(int, input().split())

account = BankAccount(initial)
account.deposit(dep)
account.withdraw(with_val)

print(account.balance())