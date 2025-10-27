class Account:
    def __init__(self, acc, balance):
        self.acc= acc
        self.balance = balance

    def debit(self , amount):
        self.balance -= amount
        print("debited amount is " ,amount)
        print("current balance is",self.bal())
    def credit(self , amount):
        self.balance += amount
        print("credited amount is " ,amount)
        print("current balance is",self.bal())
    def bal(self):
        return self.balance
    
c1 = Account(22819 , 5000)
c1.debit(1000)

class Account:
    def __init__(self , balance , acc_no , debit_amount , credit_amount):
        self.balance = balance
        self.acc_no = acc_no
        self.debit_amount = debit_amount
        self.credit_amount = credit_amount
        print("account detailes fetched",self.acc_no,"balance is ",self.balance)

    def debit(self):
        new = self.balance - self.debit_amount
        print("debited amount is",self.debit_amount,"current balance is",new)
        self.debit_amount = new
    def credit(self):
        cre = self.balance + self.credit_amount
        print("credited amount is",self.credit_amount, "current balance is",cre)
        self.credit_amount = cre

c1 = Account(3000 , 22819 , 0 , 10000)
print(c1.balance,c1.acc_no,c1.debit_amount,c1.credit_amount)
c1.credit()

