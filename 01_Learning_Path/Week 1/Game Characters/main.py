from characters import Warrior, Mage, Archer
from battle import simulate_battle

def main():
    characters = []

    while True:
        print("Menu:")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")
        choice = int(input("Choice: "))

        if choice == "1":
            print("Select character type:")
            print("1 - Warrior")
            print("2 - Mage")
            print("3 - Archer")
            type_choice = int(input("Type: "))
            name = input("Enter character name: ")

            if type_choice == 1:
                characters.append(Warrior(name))
            elif type_choice == 2:
                characters.append(Mage(name))
            elif type_choice == 3:
                characters.append(Archer(name))
            else:
                print("Invalid character type. Try again.")

        elif choice == 2:
            if characters:
                simulate_battle(characters)
            else:
                print("No characters to battle.")

        elif choice == 0:
            print("Exiting...")
            break

        else:
            print("Invalid menu choice. Try again.")

if __name__ == "__main__":
    main()