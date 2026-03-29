class Counter:
    def __init__(self):
        self.count = 0

    def addCount(self):
        self.count += 1

    def getCount(self):
        return self.count
    
    def zeroCount(self):
        self.count = 0