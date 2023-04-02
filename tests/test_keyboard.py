import pytest
from src.keyboard import KeyBoard

@pytest.fixture
def kb1():
    return KeyBoard("Logitech", 5700, 7)

def test_init(kb1):
    assert kb1.name == "Logitech"
    assert kb1.price == 5700
    assert kb1.quantity == 7
    assert kb1.language == "EN"

def test_change_lang(kb1):
    kb1.change_lang()
    assert kb1.language == "RU"
    kb1.change_lang()
    assert kb1.language == "EN"