from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename)
class Main:
    def __init__(self):

        inventory_file = FileHandler(filename)
        rows = inventory_file.read()
        print(f"### inventory ###")
        inventory = []
        for row in rows:
            _item = Item.deserialize(row)
            _item.display_price()
            inventory.append(_item)
        print(f"#### inventory ####")
        feed = input(f"Change item value (enter 1 - {len(inventory)}): ")
        try:
            index = int(feed) - 1
            feed = input(f"Set new value for {inventory[index].name}: ")
            inventory[index].set_value(float(feed))
        except Exception:
            print(f"Oops, something went wrong.")
        print(f"Serializing items into rows.")
        rows = []
        for _item in inventory:
            row = _item.serialize()
            rows.append(row)
        print(f"Saving items into '{filename}'")
        inventory_file.write(rows)
        print(f"Program ending")

if __name__ =="__main__":
    main = Main()