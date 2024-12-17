# from utils import print_menu, print_receipt_line

# def place_order(menu):
#     order = []
#     while True:
#         print_menu(menu)
#         item_number = input("\nEnter the menu item number you want to order (or 'q' to quit): ").strip()

#         if item_number.lower() == 'q':
#             break

#         order = update_order(menu, order, item_number)
#         continue_ordering = input("\nWould you like to continue ordering? (y/n): ").strip().lower()
#         if continue_ordering == 'n':
#             break

#     total_price = round(sum(item['price'] * item['quantity'] for item in order), 2)
#     return order, total_price

# def update_order(menu, order, item_number):
#     try:
#         item_number = int(item_number)
#     except ValueError:
#         print("\nInvalid menu item number. Please try again.")
#         return order

#     flat_menu = [item for items in menu.values() for item in items]
#     if item_number < 1 or item_number > len(flat_menu):
#         print("\nInvalid menu item number. Please try again.")
#         return order

#     selected_item = flat_menu[item_number - 1]
#     quantity_input = input(f"\nHow many of '{selected_item['name']}' would you like to order? ").strip()
#     try:
#         quantity = int(quantity_input)
#         if quantity < 1:
#             print("\nInvalid quantity. Defaulting to 1.")
#             quantity = 1
#     except ValueError:
#         print("\nInvalid quantity. Defaulting to 1.")
#         quantity = 1

#     order.append({'name': selected_item['name'], 'price': selected_item['price'], 'quantity': quantity})
#     print(f"\nAdded {quantity} x {selected_item['name']} to your order.")
#     return order

# def print_itemized_receipt(order, total_price):
#     print("\n--- ITEMIZED RECEIPT ---")
#     for item in order:
#         print_receipt_line(item['name'], item['price'], item['quantity'])
#     print(f"\nTotal: ${total_price:.2f}")