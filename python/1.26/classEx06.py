class Bank:
    def __init__(self,balance):
        self.__balance = balance
        
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("잔액이 부족합니다.")
        else:
            self.__balance = self.__balance - amount
        self.showBalance()        
        
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.showBalance()
        
    def showBalance(self):
        print(f"현재 잔액은 {self.__balance}입니다.")

account1 = Bank(1000000)
account1.showBalance()
account1.deposit(150)
account1.withdraw(150)