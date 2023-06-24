class Product:
    """Class made to create and edit product objects"""
    def __init__(self, name, price, quantity):
        """Initialises a products as an object with given parameters"""
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True
        self.promotion = None
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

    def get_promotion(self):
        """Returns promotion"""
        return self.promotion

    def set_promotion(self, promotion):
        """Set a promotion to the product"""
        self.promotion = promotion

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
        """Returns string with product name, price, quantity and promotion (if exist)"""
        if self.promotion:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, {self.promotion.name}"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Takes amount of product for purchase as a parameter to count
        and return total price and changes quantity of left product"""
        if self.promotion:  # if a promotion is set, the price will be calculated in promotion class method
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity  # counts a total prise of product
        if self.quantity < quantity:  # checks if product quantity enough for purchase
            raise Exception("Here is no enough product to purchase, enter less quantity.")
        self.quantity -= quantity  # changes left product quantity
        if self.quantity <= 0:  # deactivates product if it's sold out
            self.deactivate()
        return total_price


class NonStockedProduct(Product):
    """Class created to handle products which amount is unlimited to sell"""
    def __init__(self, name, price, quantity=1):
        super().__init__(name, price, quantity)
        self.quantity = quantity

    def show(self):
        """Returns string with product name, price and promotion (if exist)"""
        if self.promotion:
            return f"{self.name}, Price: ${self.price}, {self.promotion.name}"
        return f"{self.name}, Price: ${self.price}"

    def buy(self, quantity):
        """Takes amount of product for purchase as a parameter to count
        and return total price"""
        if self.promotion:  # if a promotion is set, the price will be calculated in promotion class method
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity  # counts a total prise of product
        return total_price


class LimitedProduct(Product):
    """Class created to handle products that can be purchased limited times in one order"""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Returns string with product name, price and promotion (if exist)"""
        if self.promotion:
            return f"{self.name}, Price: ${self.price}, {self.promotion.name}"
        return f"{self.name}, Price: ${self.price}"

    def buy(self, quantity):
        """Takes amount of product for purchase as a parameter to count
        and return total price and changes quantity of left product"""
        if self.promotion:  # if a promotion is set, the price will be calculated in promotion class method
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        if quantity > self.maximum:  # checks if purchased amount does not exceed set maximum
            raise Exception('You can add only 1 item of this product to your order')
        return total_price








