from player import Player
from npc import NPC
from object_entity import Object

entities = []

def menu():
    print("1 - Add Entity")
    print("2 - Interact with Entities")
    print("3 - Exit")
    return input("Choice: ")

def entity_menu():
    print("1 - Player")
    print("2 - NPC")
    print("3 - Object")
    return input("Type: ")

def add_entity():
    choice = entity_menu()
    name = input("Name: ")
    position = input("Position: ")

    if choice == "1":
        level = input("Level: ")
        entity = Player(name, position, level)
    elif choice == "2":
        role = input("Role: ")
        entity = NPC(name, position, role)
    elif choice == "3":
        obj = input("Object type: ")
        entity = Object(name, position, obj)
    else:
        print("Invalid choice")
        return
    entities.append(entity)

def interact_entities():
    if len(entities) == 0:
        print("No entities.")
        return
    for e in entities:
        e.interact()

def main():
    while True:
        choice = menu()
        if choice == "1":
            add_entity()
        elif choice == "2":
            interact_entities()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()