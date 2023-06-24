class Store:
    """Class created to manipulate the information of products in store"""
    def __init__(self, product_list):
        """Initialises a products list as an object"""
        self.product_list = product_list

    def add_product(self, product):
        """Adds given products to products list"""
        if product not in self.product_list:
            self.product_list.append(product)

    def remove_product(self, product):
        """Removes given product from products list"""
        if product in self.product_list:
            self.product_list.remove(product)
        else:
            print(f"{product} not in store")

    def get_total_quantity(self):
        """Returns total amount of products items in store"""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """Returns a list of all available products in store"""
        all_products = []
        for product in self.product_list:
            if product.active:
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        """Takes a list of tuples [(product object name, amount to order), (,), ...]
        as a parameter, manipulate products information and returns total order prise"""
        total_price = 0
        for item in shopping_list:
            product_name = item[0]  # takes product name
            for product in self.product_list:
                if product == product_name:
                    total = product.buy(item[1])  # calls buy method to get total prise for one product
                    total_price += total  # adds product total prise to final order price
        return total_price



