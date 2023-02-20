from models.todo_list import todo_list
from models.item import Item


MENU_STATE = {
    'running': True
}


class Menu:
    @classmethod
    def display(cls):
        raise NotImplementedError


    @staticmethod
    def choose_option(options:dict) -> str:
        print("Choose one of the options below:")
        print("--------------------------------")
        for opt_key in options.keys():
            print(f"\t[{opt_key}] - {options[opt_key]['description']}")

        print("--------------------------------")

        user_input = input("Answer: ").lower()
        if user_input not in options.keys():
            print(f"'{user_input}' is not a real answer...\n")
            return Menu.choose_option(options)

        return user_input


class DisplayItemsMenu(Menu):
    @classmethod
    def display(cls):
        print("--------------------------------")
        todo_list.display_items()
        print("--------------------------------")


class CreateNewItemMenu(Menu):
    @classmethod
    def display(cls) -> None:
        print("Creating a new item:\n")
        title = input("\ttitle: ")
        description = input("\tdescription: ")

        if len(title) < 2 or len(description) < 2:
            print("/!\\ Invalid attributes /!\\\n")
            create_new_item()

        item = Item(title, description)
        todo_list.add(item)

        print("Item created!")


class ExitApplicationMenu(Menu):
    @classmethod
    def display(cls):
        print("Sad to see you go :(\nExiting application...")
        MENU_STATE['running'] = False


MAIN_MENU_OPTIONS = {
    'a': {
        'description': 'Display all names',
        'action': DisplayItemsMenu.display
    },
    'c': {
        'description': 'Create a new todo item',
        'action': CreateNewItemMenu.display
    },
    'e': {
        'description': 'Exit application',
        'action': ExitApplicationMenu.display
    }
}


class MainMenu(Menu):
    @classmethod
    def display(cls) -> None:
        while MENU_STATE['running']:
            print("Hello, you currently have X things to do.\n")

            choice = Menu.choose_option(MAIN_MENU_OPTIONS)

            print("The user chose: " + choice)

            print('')
            MAIN_MENU_OPTIONS[choice]['action']()
            print('')
