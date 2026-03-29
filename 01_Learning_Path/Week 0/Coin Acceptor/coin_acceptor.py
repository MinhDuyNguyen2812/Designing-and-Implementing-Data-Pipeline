class CoinAcceptor:
    def __init__(self):
        self.amount = 0
        self.value = 0.0

    def insertCoin(self):
        self.amount += 1
        return self.amount
    
    def getAmount(self):
        print(f"Currently \'{self.amount}\' coins in coin acceptor")
        return self.amount
    
    def returnCoin(self):
        print(f"Coin acceptor returned \'{self.amount}\' coins")
        self.amount = 0
        return self.amount