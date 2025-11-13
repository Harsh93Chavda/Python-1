class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
        
    #Debit method
    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())
        
    #Credit method
    def credit(self, amount):
        self.bal += amount
        print(f"Rs.{amount}, was credited")
        print("total balance =", self.get_balance())
        
    #Total Balance
    def get_balance(self):
        return self.bal
    
acc1 = Account(10000, 73649)
acc1.debit(1000)
acc1.credit(500)
