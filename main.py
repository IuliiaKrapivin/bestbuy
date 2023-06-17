import products
import store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)]
best_buy = store.Store(product_list)


def start():
    """Prints the menu, asks a user to choose an option of menu and returns chosen number"""
    print("\n"
          "Store Menu\n"
          "___________\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit\n"
          "___________\n")
    choice = input("Please choose a number: ")
    return choice


def list_products():
    """Prints a list of all available products in store"""
    i = 0
    for item in best_buy.get_all_products():
        i += 1
        print(i, item.show())


def total_amount():
    """Prints amount of all available products in store"""
    print(f"Total of {best_buy.get_total_quantity()} items in store")


def making_order():
    """Asks a user to choose products and its amount for purchase, returns final price,
    changes products information in store"""
    shopping_list = []
    while True:  # takes a product number (in the list) and product amount to add to shopping list
        product_num = input("Which product # do you want? ")
        amount = input("What amount do you want? ")
        if product_num == "":
            break  # ands product choosing
        else:
            k = int(product_num) - 1  # turns given number to product index in the list
            product = best_buy.get_all_products()[k]  # returns exact product object
            shopping_item = (product, int(amount))  # creates a tuple to add to shopping list
            shopping_list.append(shopping_item)
            print("Product added to list!")
    return shopping_list


def main():
    """Provides a menu of options to get information about products in store and make an order"""
    while True:
        number = int(start())
        if number == 1:
            list_products()
        elif number == 2:
            total_amount()
        elif number == 3:
            list_products()
            print("When you want to finish order, press enter.")
            shopping_list = making_order()  # takes a shopping list from user
            # calls the method to manipulate with shopping list to make an order
            total_price = best_buy.order(shopping_list)
            print(f"Order made! Total payment: {total_price}")
        elif number == 4:
            print("Bye!")
            exit()


if __name__ == '__main__':
    main()

