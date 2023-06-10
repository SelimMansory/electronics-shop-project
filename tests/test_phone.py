from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def data_phone():
    return Phone("Samsung", 999.9, 10, 5)


def test_phone(data_phone):
    assert data_phone.number_of_sim == 5
    item = Item("Одеяло", 120.2, 15)
    assert data_phone+item == 25
    assert data_phone+51541 == None
    assert str(data_phone) == 'Samsung'
    assert repr(data_phone) == "Phone('Samsung', 999.9, 10, 5)"
    data_phone.number_of_sim = 10
    assert data_phone.number_of_sim == 10