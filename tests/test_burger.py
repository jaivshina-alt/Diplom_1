from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    #Тесты для класса Burger

    def test_set_buns_assigns_bun_to_burger(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        burger.set_buns(bun_mock)
        assert burger.bun is bun_mock

    def test_add_ingredient_appends_ingredient_to_list(self):
        burger = Burger()
        ingredient_mock = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients == [ingredient_mock]

    def test_add_ingredient_preserves_order(self):
        burger = Burger()
        first = Mock(spec=Ingredient)
        second = Mock(spec=Ingredient)
        third = Mock(spec=Ingredient)
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)
        assert burger.ingredients == [first, second, third]

    def test_remove_ingredient_removes_ingredient_at_index(self):
        burger = Burger()
        first = Mock(spec=Ingredient)
        second = Mock(spec=Ingredient)
        third = Mock(spec=Ingredient)
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        burger.remove_ingredient(1)

        assert burger.ingredients == [first, third]

    def test_move_ingredient_changes_ingredient_position(self):
        burger = Burger()
        first = Mock(spec=Ingredient)
        second = Mock(spec=Ingredient)
        third = Mock(spec=Ingredient)
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        burger.move_ingredient(2, 0)

        assert burger.ingredients == [third, first, second]

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_price', [
        (100, [], 200),                       # only bun, doubled
        (100, [50], 250),                     # bun*2 + one ingredient
        (200, [100, 150, 50], 700),           # bun*2 + multiple ingredients
        (0, [10, 20], 30),                    # zero-price bun
        (150.5, [49.5], 350.5),               # float prices
    ])
    def test_get_price_returns_double_bun_plus_ingredients(self, bun_price, ingredient_prices, expected_price):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = bun_price
        burger.set_buns(bun_mock)

        for price in ingredient_prices:
            ingredient_mock = Mock(spec=Ingredient)
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == expected_price

    def test_get_price_calls_get_price_on_bun_and_each_ingredient(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)

        ingredient_mock = Mock(spec=Ingredient)
        ingredient_mock.get_price.return_value = 50
        burger.add_ingredient(ingredient_mock)

        burger.get_price()

        bun_mock.get_price.assert_called()
        ingredient_mock.get_price.assert_called_once()

    def test_get_receipt_contains_bun_name_twice(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'black bun'
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)

        receipt = burger.get_receipt()

        assert receipt.count('(==== black bun ====)') == 2

    def test_get_receipt_contains_each_ingredient_with_lowercase_type(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'black bun'
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)

        sauce_mock = Mock(spec=Ingredient)
        sauce_mock.get_name.return_value = 'hot sauce'
        sauce_mock.get_type.return_value = 'SAUCE'
        sauce_mock.get_price.return_value = 100
        burger.add_ingredient(sauce_mock)

        filling_mock = Mock(spec=Ingredient)
        filling_mock.get_name.return_value = 'cutlet'
        filling_mock.get_type.return_value = 'FILLING'
        filling_mock.get_price.return_value = 200
        burger.add_ingredient(filling_mock)

        receipt = burger.get_receipt()

        assert '= sauce hot sauce =' in receipt
        assert '= filling cutlet =' in receipt

    def test_get_receipt_contains_total_price(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'black bun'
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)

        ingredient_mock = Mock(spec=Ingredient)
        ingredient_mock.get_name.return_value = 'cutlet'
        ingredient_mock.get_type.return_value = 'FILLING'
        ingredient_mock.get_price.return_value = 50
        burger.add_ingredient(ingredient_mock)

        receipt = burger.get_receipt()

        # 100 * 2 + 50 = 250
        assert 'Price: 250' in receipt

    def test_get_receipt_with_no_ingredients_has_only_buns_and_price(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'white bun'
        bun_mock.get_price.return_value = 200
        burger.set_buns(bun_mock)

        receipt = burger.get_receipt()

        expected = '(==== white bun ====)\n(==== white bun ====)\n\nPrice: 400'
        assert receipt == expected
