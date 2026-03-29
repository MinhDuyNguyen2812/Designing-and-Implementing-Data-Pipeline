from coin_acceptor import CoinAcceptor

def Options():
    value_ = float(input("Insert coin(0 return, -1 exit): "))
    return value_

def main():
    coinAcceptor = CoinAcceptor()
    print(f"Program starting.")
    print(f"Welcome to coin acceptor program.")
    print(f"Insert new coin by typing it's value (0 return the money, -1 exits the program)")
    print()

    while True:
        value_ = Options()
        if value_ == -1:
            print(f"Exiting program.")
            print()
            print("Program ending.")
            break
        elif value_ == 0:
            coinAcceptor.returnCoin()
            print()
        elif value_ > 0:
            float(value_)
            coinAcceptor.insertCoin(value_)
            print()
        else:
            print("Unvalid amount!")
            print()
    
if __name__ == "__main__":
    main()