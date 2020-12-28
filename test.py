import pytest
from click.testing import CliRunner
from unittest.mock import patch
from exam import *
import random


def test_dicts():
    """ Тест на вывод словаря """
    excepted = {"tomato_sauce": 60, "mozzarella": 150, "tomatoes": 50}
    assert Margherita(True).dicts() == excepted


@pytest.mark.parametrize(
    "test_input, exp",
    [
        (Pepperoni(False) == Pepperoni(True), False),
        (Pepperoni(True) == Pepperoni(True), True),
        (Pepperoni(True) == Margherita(True), False),
    ],
)
def test_eq(test_input, exp):
    """
    Проверяет равенство двух пицц
    """
    assert test_input == exp


def test_str():
    """ Тест на вывод str"""
    excepted = "tomato_sauce: 60, mozzarella: 150, tomatoes: 50"
    assert str(Margherita(True)) == excepted


def test_menu():
    """ Тест меню """
    runner = CliRunner()
    result = runner.invoke(menu)
    actual = result.output
    assert (
        "- Margherita" in actual and "- Hawaiian" in actual and "- Pepperoni" in actual
    )


def test_bake():
    """ Проверяет функцию готовки с декоратором """
    count = random.randint(1, 15)
    with patch.object(random, "randint", return_value=count):
        exp = f"bake - приготовили за {count} с"
        assert bake("Margherita") == exp


def test_pickup():
    """ Проверяет функцию самовывоза с декоратором """
    count = random.randint(8, 60)
    with patch.object(random, "randint", return_value=count):
        exp = f"pickup - забрали за {count} с"
        assert pickup("Margherita") == exp


def test_deliver():
    """ Проверяет функцию доставки с декоратором """
    count = random.randint(8, 60)
    with patch.object(random, "randint", return_value=count):
        exp = f"deliver - доставили за {count} с"
        assert deliver("Margherita") == exp
