# egg_shop.py
# Richie Moon
# 9/5/2022
# A program to keep track of egg inventory, adding stock, dividing stock into
# different size cartons and selling eggs to customers.

# The list of stock. They are in the format {size: quantity}.
stock = {4: 80,
         5: 0,
         6: 0,
         7: 0,
         8: 0}
all_orders = []


def print_line():
    """Prints 17 = signs. """
    print("=" * 17)


def enter_size() -> int:
    """Asks the user for the size and checks that it is valid. Will return a
    valid size, as an int. """
    while True:
        try:
            size = int(input("    > Enter Size (4-8): "))
            MAX_SIZE = 8
            MIN_SIZE = 4
            if MIN_SIZE <= size <= MAX_SIZE:
                return size
            else:
                print("    Please enter a valid size. \n")
        except ValueError:
            print("    Please enter an integer. \n")


def enter_quantity(input_message: str = None) -> int:
    """Asks the user for the quantity and checks that it is valid. Will return
    the quantity as an int. """
    while True:
        try:
            if input_message is None:
                quantity = int(input("    > Enter quantity: "))
            else:
                quantity = int(input(f"   > {input_message}: "))

            MIN_SIZE = 1
            if quantity >= MIN_SIZE:
                return quantity
            else:
                print("\n    Please enter a valid quantity. ")
        except ValueError:
            print("    Please enter an integer. \n")


def enter_carton() -> int:
    """Asks the user for the size of the carton they would like, and checks
    if it is valid. Returns the valid carton size as an int. """
    while True:
        try:
            carton_sizes = [6, 12, 24]
            carton = int(input("    > Enter carton/tray of 6, 12 or 24: "))

            if carton in carton_sizes:
                return carton
            else:
                print("    Please enter a valid carton size. \n")
        except ValueError:
            print("    Please enter an integer. ")


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

    # Call the enter_size and enter_quantity functions to ask the user for the
    # size and quantity.
    size = enter_size()
    quantity = enter_quantity()

    # Adds the quantity provided by the user to the quantity in the stock
    # dictionary.
    stock[size] += quantity
    print("    " + "-" * 17)
    print(f"    Added {quantity}x size {size} eggs. \n")


def edit_stock():
    """Will edit the number of eggs in the stock by the amount that the user
    enters. """
    print("    " + "-" * 17)
    print("      ✂️ EDIT STOCK")
    print('    ' + '-' * 17)

    size = enter_size()
    print(f"    There are currently {stock[size]}x size {size} eggs. \n")

    quantity = enter_quantity("Enter new quantity")
    print('    ' + '-' * 17)

    stock[size] = quantity

    print(f"    In Stock: {stock[size]}x size {size} eggs. \n")


def list_stock():
    """Prints the number of eggs are in stock for each size and also displays
     how many cartons of 6, 12 and 24 can be made using the number on hand. """
    print("    " + '-' * 17)
    print("      🍳 COMBINATIONS")
    print("    " + '-' * 17)

    # For every size in stock, print the size and the total number of eggs in
    # that size. Then, for every carton/tray size, check if it is 24. If it is,
    # print Trays of 24, and then how many we can make. Do the same with 6 and
    # 12 except print 'Cartons' instead of 'Trays'.
    cartons = [6, 12, 24]
    for size in stock:
        print(f"    Size {size}: {stock[size]}x")
        tray = 24
        for i in cartons:
            if i == tray:
                print(f"        - Trays of {i}: {int(stock[size] / i)}x")
            else:
                print(f"        - Cartons of {i}: {int(stock[size] / i)}x")
    print()


def sell_stock():
    """Sells eggs in cartons of 6, 12 and 24 to the customer. """
    print("\n    " + "-" * 17)
    print("      💰 SELL EGGS")
    print("   " + "-" * 17)

    order = []

    while True:
        # Asks for the size of the egg, and gets the quantity from stock. If
        # the quantity is smaller than 6 (the smallest carton size), tell that
        # to the user. Otherwise, print the available egg cartons, and ask the
        # user which size carton they would like.

        size = enter_size()
        quantity = stock[size]

        if quantity < 6:
            print(f"    There are no size {size} eggs in stock. \n")
        else:
            carton_sizes = [6, 12, 24]
            print("    You can choose from either: ")

            carton_quantity = []
            for i in carton_sizes:
                carton_quantity.append(int(quantity / i))
                print(f"        - {int(quantity / i)}x cartons of {i}")

            carton_size = enter_carton()
            index = carton_sizes.index(carton_size)

            while True:
                try:
                    carton_number = int(input("    > Enter quantity of "
                                              "cartons/trays: "))
                    if carton_number <= 0:
                        print("    Please enter a valid number. \n")
                    else:
                        break
                except ValueError:
                    print("    Please enter an integer. \n")

            if carton_number > carton_quantity[index]:
                print("\n    ⛔ INVALID QUANTITY! DID NOT MODIFY ORDER! ")
            else:
                # Calculate the price by multiplying the discount, carton
                # number and the carton size together. Round to 2dp.

                carton_sizes_and_discounts = [[6, 12, 24], [0.95, 0.9, 0.8]]
                discount_index = carton_sizes_and_discounts[0].index(
                    carton_size)

                egg_prices = [[4, 5, 6, 7, 8], [0.22, 0.26, 0.32, 0.4, 0.44]]
                size_index = egg_prices[0].index(size)

                price = round(carton_size * carton_number *
                              carton_sizes_and_discounts[1][discount_index] *
                              egg_prices[1][size_index], 2)

                # Append the users order to the list of order in a dictionary
                # with the format {size: 4, carton_size: 6, carton_number: 2,
                # price: 4.5}

                order.append({"size": size, "carton_size": carton_size,
                              "carton_number": carton_number, "price": price})

                # Remove the number of eggs sold from the stock.
                eggs_sold = carton_number * carton_size
                stock[size] -= eggs_sold

            # Print the current order and the total price.
            print("\n    - Order:")
            total_price = 0
            for item in order:
                total_price += item['price']
                print(f"        - {item['carton_number']}x cartons of "
                      f"{item['carton_size']}, size {item['size']}: "
                      f"${item['price']}")
            print(f"        - TOTAL: ${total_price}\n")

            # Ask the user if they want to order another carton of eggs.
            while True:
                cont = input("    > Add another carton/tray (yes/no): "
                             ).lower().strip()
                if cont == 'yes' or cont == 'no':
                    break
                else:
                    print("    Please enter 'yes' or 'no'. \n")

            if cont == 'yes':
                pass
            elif cont == 'no':
                break
    all_orders.append(order)
    print("-" * 17)
    print(f"Sold for ${total_price}.\n ")


def view_receipts():
    """Prints all the transactions to the user. Lists the order, carton size,
    number of cartons, egg size, and price. Prints total price for the order at
    the end. """
    print("    " + "-" * 17)
    print("       🧾 RECEIPTS")
    print("    " + "-" * 17)

    # all_orders is in the format [[{}, {}], [{}, {}]]

    for order in all_orders:
        index = all_orders.index(order)
        total_price = 0

        print(f"    Order {index + 1}: ")
        tray = 24
        
        for sub_order in order:
            if sub_order['carton_size'] == tray:
                print(f"        - {sub_order['carton_number']}x trays of "
                      f"{sub_order['carton_size']}, size {sub_order['size']}: "
                      f"${sub_order['price']}")
            
            else:
                print(f"        - {sub_order['carton_number']}x cartons of "
                      f"{sub_order['carton_size']}, size {sub_order['size']}: "
                      f"${sub_order['price']}")

            total_price += sub_order['price']
        print(f"        - TOTAL: {round(total_price, 2)} \n")


def quit_program():
    """Quits the program. """
    print("Thank you for using Eggshop. ")
    quit()


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
                        [add_stock, edit_stock, list_stock,
                         sell_stock, view_receipts, quit_program]]

        # The index of the letters and the function names in the menu_choices
        # list. Find the index of the letter that the user entered, and use
        # that to call the actual function.
        LETTERS = 0
        FUNCTION_NAMES = 1

        index = menu_choices[LETTERS].index(user_choice)
        menu_choices[FUNCTION_NAMES][index]()


main()
