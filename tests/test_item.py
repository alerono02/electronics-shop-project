"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *

item1 = Item("phone", 1000, 5)


def test_item():
    # Testcase№1 test calculate
    assert 1000 * 5 == item1.calculate_total_price()
    # Testcase№2 test discount
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 800


def test_second():
    # Testcase№3 get name
    assert item1.name == "phone"
    # Testcase№4 set name
    item1.name = "abcdefghijklmnop"
    assert item1.name == 'abcdefghij'
    # Testcase№5 instantiate from csv
    Item.all=[]     # clean the list, bcs item1 instand in Item.all
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    # Testcase№6 transform number
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('15.55') == 15
    assert Item.string_to_number('37.78456') == 37
