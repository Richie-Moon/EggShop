# egg_shop.py
# Richie Moon
# 9/5/2022
# A program to keep track of egg inventory, adding stock, dividing stock into
# different size cartons and selling eggs to customers.

# The list of stock. They are in the format {size: quantity}.
stock = {4: 0,
         5: 0,
         6: 0,
         7: 0,
         8: 0}


def print_line():
    print("=" * 17)


def print_menu():
    """Will print the main menu and menu items when called. """
    print_line()
    print("   🥚 EGGSHOP")
    print_line()
    menu_items = {"A": "Add Eggs to Stock.",
                  "E": "Edit egg stock and possible combinations. ",
                  "L": "List stock. ",
                  "S": "Sell Eggs. ",
                  "R": "View receipts. ",
                  "Q": "Quit. "}
    for key, value in menu_items.items():
        print(f"{key}: {value}")
    print_line()


def is_valid_choice(choice: str) -> bool:
    """Takes an input 'choice' and checks if it in the list of valid_choices.
    Return True if it is, False if it isn't. """

    valid_choices = ["a", "e", "l", "s", "r", "q"]
    if choice in valid_choices:
        return True
    else:
        return False


def add_stock():
    """Will ask the user for the size and quantity to increase stock by."""
    print("\n    " + "-" * 17)
    print("       ➕ ADD EGGS")
    print("    " + "-" * 17)

    # Try to convert the user input to an integer. If it fails, prints Please
    # enter an integer, and asks again. Does this for both the size and the
    # quantity.
    while True:
        try:
            size = int(input("    > Enter size (4-8): "))
            MAX_SIZE = 8
            MIN_SIZE = 4
            if MIN_SIZE <= size <= MAX_SIZE:
                break
            else:
                print("    Please enter a valid size (4-8). \n")
        except ValueError:
            print("    Please enter an integer. \n")

    while True:
        try:
            quantity = int(input("    > Enter quantity: "))
            MIN_SIZE = 1
            if quantity >= MIN_SIZE:
                break
            else:
                print("\n    Please enter a valid quantity. ")
        except ValueError:
            print("    Please enter an integer. \n")

    # Adds the quantity provided by the user to the quantity in the stocks
    # dictionary.
    stock[size] += quantity
    print("    " + "-" * 17)
    print(f"    Added {quantity}x size {size} eggs. \n")


def main():
    """This function will ask the user for their choice and check that it's
    valid. It will then call the other functions that the user asked for. """
    while True:
        print_menu()
        user_choice = input("> Enter a choice: ").strip().lower()
        valid_answer = is_valid_choice(user_choice)

        # While loop, which says sorry if the user answer is not valid,
        # and then asks the user for another choice, which gets checked.
        while valid_answer is False:
            print("Sorry, that's not a valid choice. \n")
            print_menu()

            user_choice = input("> Enter a choice: ").lower().strip()
            valid_answer = is_valid_choice(user_choice)

        menu_choices = [["a", "e", "l", "s", "r", "q"],
                        [add_stock]]

        # The index of the letters and the function names in the menu_choices
        # list. Find the index of the letter that the user entered, and use
        # that to call the actual function.
        LETTERS = 0
        FUNCTION_NAMES = 1

        index = menu_choices[LETTERS].index(user_choice)
        menu_choices[FUNCTION_NAMES][index]()


main()
