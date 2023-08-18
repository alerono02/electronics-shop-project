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
