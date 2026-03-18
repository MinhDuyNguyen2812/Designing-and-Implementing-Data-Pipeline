class CoinAcceptor:
    def __init__(self):
        self.amount = 0
        self.value = 0.0

    def insertCoin(self, value_):
        self.amount += 1
        self.value += value_
        print(f"Inserted coins = {self.amount}, value = {self.value}€")
        return (self.amount, self.value)
    
    def returnCoin(self):
        print(f"{self.amount} coins with {self.value}€ value returned")
        self.amount = 0
        self.value = 0
        print(f"Inserted coins = {self.amount}, value = {self.value}€")
        return (self.amount, self.value)