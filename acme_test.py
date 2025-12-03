import pytest
from acme import Product
from acme_report import generate_products


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product("Test Product")
    assert prod.price == 10


def test_default_product_weight():
    """Test default product weight being 20."""
    prod = Product("Test Product")
    assert prod.weight == 20


def test_stealability_and_explode():
    """Test the stealability and explode methods."""
    prod = Product("Test", price=10, weight=20, flammability=0.5)
    assert prod.stealability() == "Kinda stealable."
    assert prod.explode() == "...boom!"


def test_generate_products_default_length():
    """Test that generate_products returns 30 items by default."""
    products = generate_products()
    assert len(products) == 30
