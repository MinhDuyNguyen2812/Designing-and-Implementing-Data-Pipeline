from coin_acceptor import CoinAcceptor

def showOptions():
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")
    choice  = int(input("Your choice: "))
    return choice 

def main():
    coinAcceptor = CoinAcceptor()
    print(f"Program starting.")
    while True:
        choice = showOptions()
        if choice == 1:
            coinAcceptor.insertCoin()
            print()
        elif choice == 2:
            coinAcceptor.getAmount()
            print()
        elif choice == 3:
            coinAcceptor.returnCoin()
            print()
        elif choice == 0:
            break
        else:
            print("Unknown option!")
            print()

if __name__ == "__main__":
    main()