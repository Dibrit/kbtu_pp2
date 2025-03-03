class Account:
    def __init__(self, a, b):
        self.owner = a
        self.bal = b

    def deposit(self, a):
        self.bal += a
        print(f"New balance: {self.bal}")

    def withdraw(self, a):
        if a > self.bal:
            print("not enough money")
        else:
            self.bal -= a
            print(f"New balance: {self.bal}")
            
b = input()
a = int(input()) 
account = Account(b, a)
while True:
    a = int(input())
    if a == 1 :
        b = int(input())
        account.deposit(b)
    elif a == 2 :
        b = int(input())
        account.withdraw(b)
