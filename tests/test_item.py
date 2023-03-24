"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
import csv
@pytest.fixture
def item1():
    return Item('Смартфон', 10000, 20)

def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_calculate_total_price(item1):
    assert item1.price*item1.quantity == 200000

def test_apply_discount(item1):
    assert item1.price*item1.pay_rate == int(10000)


def test_string_to_number():
    assert Item.string_to_number('43.9') == 43

def test_name():
    Item.name = "Новыйсмартфон"
    assert Item.name == "Новыйсмартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(CSV_FILE='../src/items.csv')
    assert type(Item.all) is not None

def test__str__(item1):
    assert str(item1) == 'Смартфон'


def test__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
