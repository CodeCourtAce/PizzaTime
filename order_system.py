def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to GGs Pizza and More Restaurant.")

    place_order = True
    # Create a continuous while loop so customers can order multiple items
    while place_order:
        # Initialize a counter for menu item numbers
        item_number = 1

        # Loop through the menu dictionary, extracting the food category and
        # the options for each category
        for food_category, options in menu.items():
            # Loop through the options for each food category, extracting the
            # meal and the price
            for meal, price in options.items():
                # Print the menu item number, food category, meal, and price
                print_menu_line(item_number, food_category, meal, price)
                item_number += 1

        # Ask customer to input menu item number
        menu_selection = input("Type menu number: ")

        # Update the order list using the update_order function
        # Send the order list, menu selection, and menu items as arguments
        order = update_order(order, menu_selection, menu_items)

        # Ask the customer if they would like to order anything else
        # Let the customer know if they should type 'n' or 'N' to quit
        keep_ordering = input("Would you like to keep ordering? (N) to quit: ")

        # Write a conditional statement that checks if the customer types
        # 'n' or 'N'
        if keep_ordering.lower() == 'n':
            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order.")

            # Use a list comprehension to create a list called prices_list,
            # which contains the total prices for each item in the order list:
            prices_list = [item["Price"] * item["Quantity"] for item in order]

            # Create an order_total from the prices list using sum()
            order_total = round(sum(prices_list), 2)

            # Exit the ordering loop
            place_order = False

    # Return the order list and the order total
    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                             prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered (updated as needed).
    """
    try:
        # Convert the menu selection to an integer
        menu_selection = int(menu_selection)
    except ValueError:
        print("Invalid menu selection. Please enter a valid menu number.")
        return order

    # Check if the selection is valid
    if menu_selection not in menu_items:
        print("That was not a menu option. Please enter a valid menu number.")
        return order

    # Store the item name and price
    item_name = menu_items[menu_selection]["Item name"]
    item_price = menu_items[menu_selection]["Price"]

    # Ask the customer for quantity
    quantity_input = input(f"How many of '{item_name}' would you like to order? ")
    try:
        quantity = int(quantity_input)
        if quantity < 1:
            raise ValueError
    except ValueError:
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1

    # Add the item to the order list
    order.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
    print(f"Added {quantity} x '{item_name}' to your order.")
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        print_receipt_line(item_name, price, quantity)


##################################################
#  STARTER CODE
##################################################

def print_receipt_line(item_name, price, quantity):
    num_item_spaces = 32 - len(item_name)
    item_spaces = " " * num_item_spaces
    print(f"{item_name}{item_spaces}| ${price:.2f} | {quantity}")


def print_receipt_heading():
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("----------------------------------------------------")


def print_receipt_footer(total_price):
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_line(index, food_category, meal, price):
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    i_spaces = " " * (6 if index < 10 else 5)
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price:.2f}")


def get_menu_items_dict(menu):
    menu_items = {}
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            menu_items[i] = {"Item name": f"{food_category} - {meal}", "Price": price}
            i += 1
    return menu_items


def get_menu_dictionary():
    meals = {
        "Burrito": {"Chicken": 4.49, "Beef": 5.49, "Vegetarian": 3.99},
        "Rice Bowl": {"Teriyaki Chicken": 9.99, "Sweet and Sour Pork": 8.99},
        "Sushi": {"California Roll": 7.49, "Spicy Tuna Roll": 8.49},
        "Noodles": {"Pad Thai": 6.99, "Lo Mein": 7.99, "Mee Goreng": 8.99},
        "Pizza": {"Cheese": 8.99, "Pepperoni": 10.99, "Vegetarian": 9.99},
        "Burger": {"Chicken": 7.49, "Beef": 8.49},
    }
    return meals


# Run the program
if __name__ == "__main__":
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    print("\nThis is what you ordered! :\n")
    print_receipt_heading()
    print_itemized_receipt(receipt)
    print_receipt_footer(total_price)
    print("\nThank you for ordering with us. Enjoy your meal! :)")
