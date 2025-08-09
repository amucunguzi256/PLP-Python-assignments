
class Transaction:
    def __init__(self,amount,transaction_type,balance):
        self.balance=balance
        self.amount=amount
        self.transaction_type=transaction_type

class Account:
    def __init__(self,student_name,account_number,balance=0):
        self.student_name=student_name
        self.account_number=account_number
        self.__balance=balance
        self.__locked= False
        self.transactions=[]

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__balance= amount    
        else:
            print("Amount cannot be negative")

    @property
    def locked(self):
        return self.__locked
    
    @locked.setter
    def locked(self,status):
        self.__locked = status
       
    def lock_account(self):
        self.locked = True
        print(f"Account for {self.student_name} is now LOCKED.")

    def unlock_account(self):
        self.locked = False
        print(f"Account for {self.student_name} is now UNLOCKED.")
    
    def deposit(self,amount):
        if self.locked:
            print("Account is locked, deposits not allowed")
            return
        if amount>=1000:
            self.balance+=amount
            self.transactions.append(Transaction(amount,"Deposit",self.balance))
            print(f"\n{self.student_name}---> Account Number: {self.account_number}; has deposited Ksh:{amount};\nBalance is: Ksh:{self.balance}")
        else:
            print("\nAmount must be greater than 1000")
    def withdraw(self,amount):
        if self.locked:
            print("Account is locked, withdrawal not allowed")
            return

    def display_transaction(self,student_name):
        if len(self.transactions)>0:
            print(f"\n--------------------\nTransaction history for {student_name}\n--------------------")
            for i, transaction in enumerate(self.transactions,start=1):
                print(f"\n{i}. Ksh:{transaction.amount} --> {transaction.transaction_type};Balance = Ksh:{transaction.balance}")
        else:
            print("No transactions so far!")
class Day_student(Account):
    def __init__(self, student_name, account_number, balance=0):
        super().__init__(student_name, account_number, balance)
    def withdraw(self,amount):
        if self.locked:
            print("Account is locked, withdrawal not allowed")
            return
        if amount>self.balance:
            print("Insufficient funds... Deposit money into your account")
        elif amount<=self.balance and amount<=1000:
            self.balance-=amount
            self.transactions.append(Transaction(amount,"Withdraw",self.balance))
            print(f"\n{self.student_name} has withdrawn Ksh:{amount} from Account Number:{self.account_number};\nBalance is:Ksh:{self.balance}")
        else:
            print("Day students cannot withdraw more than 1000")

class Boarding_student(Account):
    def __init__(self, student_name, account_number, balance=0):
        super().__init__(student_name, account_number, balance)

    def withdraw(self,amount):
        if self.locked:
            print("Account is locked, withdrawal not allowed")
            return
        if amount>self.balance:
            print("Insufficient funds... Deposit money into your account")
        elif amount<=self.balance and amount<=2000:
            self.balance-=amount
            self.transactions.append(Transaction(amount,"Withdraw",self.balance))
            print(f"\n{self.student_name} has withdrawn Ksh:{amount} from Account Number:{self.account_number};\nBalance is:Ksh:{self.balance}")
        else:
            print("Boarding students cannot withdraw more than 2000")


if __name__=="__main__":
    while True:
        
        name= input("Please input the student's name: ")
        account_number = int(input("Please input the account number: "))
        try:
            school_type = input("Please specify whether you are in Day or Boarding: ").strip().lower()
            if school_type =="day" or school_type =="boarding":
                break
            else:
                print("\nEnter either day or boarding; Try again!")
                continue
        except:
            print("Invalid option")
            continue
       
    if school_type == "day":
        acc= Day_student(name,account_number)
    elif school_type =="boarding":
        acc= Boarding_student(name,account_number)
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Lock\n4. Unlock\n5. Show Balance\n6. Show Transactions\n7. Exit")
        choice = input("Choose an option: ")
        try:
            if choice == "1":
                amt = int(input("Amount to deposit: "))
                acc.deposit(amt)
            elif choice == "2":
                amt = int(input("Amount to withdraw: "))
                acc.withdraw(amt)
            elif choice == "3":
                acc.lock_account()
            elif choice == "4":
                acc.unlock_account()
            elif choice == "5":
                print(f"\nCurrent Balance: Ksh {acc.balance}")
            elif choice == "6":
                acc.display_transaction(name)
            elif choice == "7":
                print("\nThank you for using the School Bursar application; Good bye---")
                break
        except:
            print("Invalid option.")
