from dataclasses import dataclass

@dataclass
class Item:
    SEPARATOR = ","
    name: str
    value: float
    category: str
    weight: float

    @staticmethod
    def deserialize(row):
        columns = row.split(Item.SEPARATOR)
        item = Item(
            columns[0],
            columns[1],
            columns[2],
            columns[3]
        )
        return item
    
    def display_price(self):
        print(f"{self.name} costs{self.value} euros.")

    def serialize(self):
        columns = []
        columns.append(self.name)
        columns.append(str(self.value))
        columns.append(self.category)
        columns.append(str(self.weight))
        row = Item.SEPARATOR.join(columns)
        return row
    
    def set_value(self, new_value):
        if new_value < 0:
            print(f"Value can't be negative.")
        else:
            self.value = new_value
        return None
        