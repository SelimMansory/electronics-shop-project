"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_init():
    item = Item('test', 200.0, 100)
    Item.pay_rate = 0.5
    item.name = "test2"
    with pytest.raises(Exception):
        item.name = "1234567890l"
    assert item.name == 'test2'
    assert item.price == 200.0
    assert item.quantity == 100
    item.apply_discount()
    assert item.calculate_total_price() == 10000.0

    Item.instantiate_from_csv()
    assert len(Item.all) == 6
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.5') == 5