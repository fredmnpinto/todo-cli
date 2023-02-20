from models.item import Item

class TodoList:
    def __init__(self) -> None:
        self.items = []

    def populate(self, items:list) -> None:
        self.items += items

    def add(self, item:Item) -> None:
        self.items.append(item)

    def to_csv(self) -> str:
        csv_values = ""

        for i in self.items:
            csv_values += i.to_csv() + ",\n"

        return csv_values

    def display_items(self) -> None:
        print(f"Items({len(self.items)}):\n")
        for i in self.items:
            print(i)

todo_list = TodoList()
