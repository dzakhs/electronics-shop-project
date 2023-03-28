import pytest
from src.phone import Phone

@pytest.fixture
def phone1():
    return Phone("Xaomi", 100_000, 15, 2)

def test_phone_init(phone1):
    assert phone1.name == "Xaomi"
    assert phone1.price == 100_000
    assert phone1.quantity == 15
    assert phone1.number_of_sim == 2

def test_str(phone1):
    assert str(phone1) == "Xaomi"

def test_repr(phone1):
    assert repr(phone1) == "Phone('Xaomi', 100000, 15, 2)"


def test_number_of_sim(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0