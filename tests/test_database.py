from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    #Тесты для класса Database

    def test_available_buns_returns_list_of_buns(self):
        database = Database()
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_buns_contains_expected_buns(self):
        database = Database()
        buns = database.available_buns()
        bun_names_and_prices = [(bun.get_name(), bun.get_price()) for bun in buns]
        assert ('black bun', 100) in bun_names_and_prices
        assert ('white bun', 200) in bun_names_and_prices
        assert ('red bun', 300) in bun_names_and_prices

    def test_available_ingredients_returns_list_of_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    def test_available_ingredients_contains_three_sauces(self):
        database = Database()
        ingredients = database.available_ingredients()
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_available_ingredients_contains_three_fillings(self):
        database = Database()
        ingredients = database.available_ingredients()
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
