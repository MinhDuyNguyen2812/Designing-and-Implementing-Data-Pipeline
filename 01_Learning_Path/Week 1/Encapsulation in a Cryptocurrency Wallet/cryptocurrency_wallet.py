from dataclasses import dataclass

@dataclass
class CryptoWallet:
    __balance: float
    __walletId: str

    @staticmethod
    def CreateWallet(walletId, balance):
        return CryptoWallet(balance, walletId)

    def Deposit(self, amount):
        if amount < 0:
            print(f"Amount can not be neagtive.")
        else:
            self.__balance += amount
        return None
    
    def Withdraw(self, amount):
        if amount < 0:
            print(f"Amount can not be nagative.")
        elif amount > self.__balance:
            print(f"Amount can not be greater than balance.")
        else:
            self.__balance -= amount
        return None
    
    def CheckBalance(self):
        print(f"Current balance of wallet '{self.__walletId}' is: {self.__balance} euros.")
        return None
    
    def TransactionHistory(self):
        return None
    
