from counter import Counter

def showOptions():
    print(f"Options:")
    print(f"1) Add count")
    print(f"2) Get count")
    print(f"3) Zero count")
    print(f"0) Exit program")

def main():
    print(f"Program starting.")
    print(f"Initializing counter...")
    print(f"Counter initialized.\n")
    counter = Counter()
    while True:
        showOptions()
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print(f"Invalid input, please enter a number.\n")
            continue

        if choice == 1:
            counter.addCount()
            print(f"Count increased\n")
        elif choice == 2:
            print(f"Current count \'{counter.getCount()}\'\n")
        elif choice == 3:
            counter.zeroCount()
            print(f"Count zeroed\n")
        elif choice == 0:
            print(f"Program ending.")
            break
        else:
            print(f"Invalid choice, try again\n")
        
if __name__ == "__main__":
    main()