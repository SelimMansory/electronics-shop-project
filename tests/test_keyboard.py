from src.keyboard import Keyboard
import pytest



def test_Keyboard():
    keyboard = Keyboard('Logitech', 1000.0, 10)
    assert str(keyboard) == 'Logitech'
    assert keyboard.__dict__ == {'_Item__name': "Logitech", '_MixinLog__language': 'EN', 'price': 1000.0, "quantity": 10}
    assert repr(keyboard) == "Keyboard('Logitech', 1000.0, 10)"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == 'EN'