class Bank:
    def __init__(self,ac,n1,t1,b1):
        self.accntno=ac
        self.name=n1
        self.type=t1
        self.balance=b1

    def deposit(self,amnt):
        self.balance+=amnt
        print("Balance:",self.balance)

    def withdraw(self, amnt):
        if(self.balance>amnt):
            self.balance-= amnt
            print("Balance:", self.balance)

        else:
            print("Balance is too low")

b=Bank(13248,'Anusha','Savings',10000)
a=int(input("Enter amount to deposit:"))
b.deposit(a)
w=int(input("Enter amount to withdraw:"))
b.withdraw(w)