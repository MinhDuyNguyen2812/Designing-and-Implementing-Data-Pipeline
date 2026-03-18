from file_handler import FileHandler
from cryptocurrency_wallet import CryptoWallet

filename = "user_data.csv"
user_file = FileHandler(filename)
rows = user_file.read()

def showOptions():
    print(f"Menu:")
    print(f"1 - Create wallet")
    print(f"2 - Deposit")
    print(f"3 - Withdraw")
    print(f"4 - Check balance")
    print(f"5 - Transaction history")
    print(f"0 - Exit program")
    
def main():
    print(f"Welcome to cryptocurrency wallet system!")
    while True:
        showOptions()
        try:
            Choice = int(input("Choice: "))
        except ValueError:
            print(f"Invalid choice.")
            continue

        if Choice == 1:
            wallet_id = input("Enter wallet id: ")
            balance = float(input("Enter initial balance: "))
            wallet = CryptoWallet.CreateWallet(wallet_id, balance)
            print(f"Wallet created with id '{wallet_id}' and balance {balance} euros.")
        elif Choice == 2:
            if wallet is None:
                print(f"Create a wallet first.")
            else:
                amount = float(input("Enter an amount to deposit: "))
                wallet.Deposit(amount)
        elif Choice == 0:
            print(f"Thank you for using.")
            break
        else:
            print(f"Invalid choice.")

if __name__ =="__main__":
    main()