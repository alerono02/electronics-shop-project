"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *
from src.phone import *
from src.keyboard import *


@pytest.fixture()
def test_item():
    item1 = Item("phone", 1000, 5)
    return item1


@pytest.fixture()
def test_item2():
    item2 = Phone('iPhone', 10000, 3, 1)
    return item2


def test_first(test_item):
    # Testcase№1 test calculate
    assert 1000 * 5 == test_item.calculate_total_price()
    # Testcase№2 test discount
    Item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 800


def test_second(test_item):
    # Testcase№3 get name
    assert test_item.name == "phone"
    # Testcase№4 set name
    test_item.name = "electronic_device"
    assert test_item.name == 'electronic'
    # Testcase№5 instantiate from csv
    Item.all = []  # clean the list, bcs item1 instand in Item.all
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    # Testcase№6 transform number
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('15.55') == 15
    assert Item.string_to_number('37.78456') == 37


def test_third(test_item):
    assert repr(test_item) == "Item('phone', 1000, 5)"
    assert str(test_item) == 'phone'


def test_fourth(test_item, test_item2):
    assert str(test_item2) == 'iPhone'
    assert repr(test_item2) == "Phone('iPhone', 10000, 3, 1)"
    assert test_item + test_item2 == 8


def test_fifth():
    kb = Keyboard('Razer', 1500, 3)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
    try:
        kb.language = 'CH'
        raise AssertionError
    except AttributeError:
        pass
