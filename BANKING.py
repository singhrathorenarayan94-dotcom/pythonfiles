class bank :
    def __init__(self,acno,bal):
        self.bal = bal 
        self.acno = acno
    def dep(self):
        n = int(input("enter the amount u want to deposite "))
        self.bal+=n
        print("your current balance is:",self.bal)
    def wid(self):
        n = int(input("enter the amount u want to withdraw :"))
        if n < self.bal:
            self.bal-=n
            print("your current balance is:",self.bal)
        else:
            print("you don't have enough money")
    def dis(self):
        print("your account no is:",self.acno)
        print("your balance is ",self.bal)
b = {}
while True:
    ch = int(input("enter 1 to create and account \n enter 2 if u have an account \n press 3 for exit"))
    match ch:
        case 1:
            acno = int(input("enter the account u want to create:"))
            bal = int(input("enter the inital deposite in your account:"))
            if acno not in b:
                b[acno]=bank(acno,bal)
            else:
                print("esa account no pahle se exist  karta")
        case 2:
            acno = int(input("enter your account no.:"))
            if acno in b:
                while True:
                    o=b[acno]
                    choice = int(input("for deposite press 1 \nfor withdraw press 2 \nfor display account details press 3 \n press 4 for exit"))
                    match choice :
                        case 1:
                            o.dep()
                        case 2:
                            o.wid()
                        case 3:
                            o.dis()
                        case 4:
                            break
            else:
                print("ye account no exist nahi karta")
        case 3:
            break

