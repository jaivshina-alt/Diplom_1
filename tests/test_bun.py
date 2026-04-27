import pytest

from praktikum.bun import Bun


class TestBun:
    #Тесты для класса Bun

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200.5),
        ('red bun', 0),
        ('', 50),
    ])
    def test_get_name_returns_name_from_constructor(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200.5),
        ('red bun', 0),
        ('cheap bun', 0.01),
    ])
    def test_get_price_returns_price_from_constructor(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
