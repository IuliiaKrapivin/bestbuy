class Product:
    """Class made to create and edit product objects"""
    def __init__(self, name, price, quantity):
        """Initialises a products as an object with given parameters"""
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True
        if name == "":
            raise Exception('Error, enter correct name')
        if price <= 0:
            raise Exception('Error, price should be positive')
        if quantity <= 0:
            raise Exception('Error, quantity should be positive')

    def get_quantity(self):
        """Returns product quantity"""
        return self.quantity

    def set_quantity(self, quantity):
        """Changes product quantity with given parameter, if quantity is 0, deactivates it"""
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """Checks if product is active"""
        if self.active:
            return True
        else:
            return False

    def activate(self):
        """Activates product"""
        self.active = True

    def deactivate(self):
        """Deactivates product"""
        self.active = False

    def show(self):
        """Returns string with product, price and quantity"""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Takes amount of product for purchase as a parameter to count
        and return total price and changes quantity of left product"""
        total_price = self.price * quantity  # counts a total prise of product
        if self.quantity < quantity:  # checks if product quantity enough for purchase
            raise Exception("Here is no enough product to purchase, enter less quantity.")
        self.quantity -= quantity  # changes left product quantity
        if self.quantity <= 0:  # deactivates product if it's sold out
            self.deactivate()
        return total_price
