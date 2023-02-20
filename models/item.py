import time

class Item:
    def __init__(self, title, description) -> None:
        self.created_at = time.time()
        self.title = title
        self.description = description
        self.done = False

    def to_csv(self) -> str:
        return f"{self.created_at},{self.title},{self.description},{self.done}"

    def __repr__(self):
        return f"Item:\n\tcreated_at: {time.ctime(self.created_at)}\n\ttitle: {self.title}\n\tdescription: {self.description}\n\tdone: {self.done}"
