import pytest

from praktikum.bun import Bun


class TestBun:
    #Тесты для класса Bun

    @pytest.mark.parametrize('name', [
        'black bun',
        'white bun',
        'red bun',
        '',
    ])
    def test_get_name_returns_name_from_constructor(self, name):
        bun = Bun(name, price=100)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [
        100,
        200.5,
        0,
        0.01,
    ])
    def test_get_price_returns_price_from_constructor(self, price):
        bun = Bun('black bun', price)
        assert bun.get_price() == price
