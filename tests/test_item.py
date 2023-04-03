"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
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
    try:
        Item.instantiate_from_csv('../tests/items_wrong.csv')
    except InstantiateCSVError:
        print('Файл item.csv поврежден')
    try:
        Item.instantiate_from_csv('../src/something.csv')
    except FileNotFoundError:
        print("Отсутствует файл item.csv")

def test__str__(item1):
    assert str(item1) == 'Смартфон'


def test__repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_add():
    item = Item("Смартфон", 10000, 20)
    phone = Phone("Xaomi", 100_000, 15, 2)
    assert item + phone == 35
    with pytest.raises(ValueError):
        phone + 10

def test_InstantiateCSVError():
    error = InstantiateCSVError()
    assert error.__str__() == "Файл item.csv поврежден"