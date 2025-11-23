class account:
    def __init__(self,Name,Balance,Account_no):
        self.name= Name
        self.balance= Balance
        self.accountno = Account_no
        self.histry= []

    def __str__(self):
         return f"Account Holder: {self.name}, Account No: {self.accountno}, Balance: Rs. {self.balance}"         

    def get_balance(self):
         return self.balance        

    def debit(self,amount):
        if amount <=0:
             print("Amount is must be greater than Zero")
             return
        if amount>self.balance:
             print("Insufficient Balance")
             return
        else:
             self.balance -= amount
             print("Rs.",amount,"was debited")
             print("total balance =", self.get_balance())

    def credit(self,amount) :
           self.balance += amount
           print("Rs.",amount,"was Credited")
           print("total balance =", self.get_balance())

Person1= account("Akash",10000,"SBI00254012")
Person1.credit(200000)
Person1.debit(5000)
Person1.debit(300000)
Person1.credit(500000)
print(Person1)

Person2=account("Atharv",200000,"HDFC00524689")
Person2.credit(100000)
Person2.debit(500000)
Person2.credit(70000)
Person2.debit(100000)
print(Person2)

Person3=account("Ronit",500000,"UBI008529412")
Person3.debit(200000)
Person3.credit(100000)
Person3.credit(300000)
Person3.debit(50000)
print(Person3)
