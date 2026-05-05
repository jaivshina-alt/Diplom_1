import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    #Тесты для класса Ingredient

    @pytest.mark.parametrize('price', [
        100,
        200.5,
        0,
        0.01,
    ])
    def test_get_price_returns_price_from_constructor(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', [
        'hot sauce',
        'cutlet',
        '',
    ])
    def test_get_name_returns_name_from_constructor(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, price=100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type_returns_type_from_constructor(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'hot sauce', price=100)
        assert ingredient.get_type() == ingredient_type
