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