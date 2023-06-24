from abc import ABC, abstractmethod


class Promotion(ABC):
    """The class is abstract, created to handle promotions conditions"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Method takes product and its quantity as a parameters, applies promotion condition and returns final price"""
        pass


class PercentDiscount(Promotion):
    """Class created to apply a percent discount to a product price"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        price = product.price
        final_price = price * ((100 - self.percent) / 100) * quantity  # calculates the cost minus the discount
        return final_price


class SecondHalfPrice(Promotion):
    """Class created to calculate the price for promotion the second item of the product with the 50% discount"""
    def apply_promotion(self, product, quantity):
        price = product.price
        if quantity % 2 == 0:
            final_price = (price + (price / 2)) * quantity / 2
        else:
            half_price = (quantity // 2) * price / 2  # counts how many items will have a 50% discount and their price
            final_price = (price * quantity) - half_price
        return final_price


class ThirdOneFree(Promotion):
    """Class created to calculate the price for promotion the third item of the product is for free"""
    def apply_promotion(self, product, quantity):
        price = product.price
        if quantity % 3 == 0:
            final_price = (price * 2) * quantity/3
        else:
            third_free = (quantity // 3) * price  # counts how many items will be for free and their price
            final_price = (price * quantity) - third_free
        return final_price

