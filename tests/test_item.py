"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *


@pytest.fixture
def start_data():
    return Item("Пижама", 999.9, 10)


def test_Item(start_data):
    assert start_data.name == 'Пижама'
    start_data.name = 'Шкаф'
    assert start_data.name == 'Шкаф'
    start_data.name = 'СлишкомДлинноеСлово'
    assert start_data.name == 'Шкаф'
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert start_data.string_to_number('50.1') == 50
    start_data.instantiate_from_csv()
    assert start_data.all[1].price == '100'
    assert repr(start_data) == "Item('Шкаф', 999.9, 10)"
    assert str(start_data) == 'Шкаф'
    assert start_data + start_data == 20
    assert start_data + 573745 == None


def test_calculate_total_price(start_data):
    assert start_data.calculate_total_price() == 999.9 * 10


def test_apply_discount(start_data):
    start_data.apply_discount()
    assert start_data.price == 999.9


def test_instantiate_from_csv_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path=('wrong.csv'))


def test_instantiate_from_csv_error_file():
    with pytest.raises(InstantiateCSVFile):
        Item.instantiate_from_csv(path=('../src/error.csv'))


def test_InstantiateCSVFile():
    csvfile = InstantiateCSVFile()
    assert str(csvfile) == 'Файл item.csv поврежден'
