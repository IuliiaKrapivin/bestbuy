import pytest
import products


def test_create_product():
    """Test for creating a product"""
    iphone = products.Product("iPhone 14 128GB Apple", price=1000, quantity=50)
    assert iphone.show() == "iPhone 14 128GB Apple, Price: $1000.0, Quantity: 50"


def test_creating_with_name_exception():
    """Test for creating a product with empty name string"""
    with pytest.raises(Exception, match='Error, enter correct name'):
        iphone = products.Product("", price=1000, quantity=50)


def test_creating_with_price_exception():
    """Test for creating a product with negative price"""
    with pytest.raises(Exception, match='Error, price should be positive'):
        iphone = products.Product("iPhone 14 128GB Apple", price=-1000, quantity=50)


def test_zero_quantity():
    """Test to check product activity"""
    iphone = products.Product("iPhone 14 128GB Apple", price=1000, quantity=50)
    iphone.set_quantity(0)
    assert iphone.is_active() == False


def test_purchase_quantity():
    """Test to check quantity changing"""
    iphone = products.Product("iPhone 14 128GB Apple", price=1000, quantity=50)
    iphone.buy(5)
    assert iphone.get_quantity() == 45


def test_larger_quantity():
    """Test to check quantity exception (in case if purchased more items that is in store)"""
    iphone = products.Product("iPhone 14 128GB Apple", price=1000, quantity=50)
    with pytest.raises(Exception, match="Here is no enough product to purchase, enter less quantity."):
        iphone.buy(55)

