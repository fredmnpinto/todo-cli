from models.item import Item
from models.todo_list import TodoList
from menu import MainMenu

if __name__ == "__main__":
    i = Item('Clean the dishes', 'I need to clean the dishes before mom gets home at 20:00!')
    tl = TodoList()

    tl.add(i)

    MainMenu.display()
