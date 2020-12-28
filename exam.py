from typing import Callable, Dict

import click
import random


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--pick", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool, pick: bool) -> None:
    """ Принимает заказ и выводит этапы жизни пиццы"""
    click.echo(bake(pizza))
    if delivery:
        click.echo(deliver(pizza))
    elif pick:
        click.echo(pickup(pizza))


@cli.command()
def menu() -> None:
    """ Выводит меню """
    print(f"- Margherita 🧀 : " f"{str(Margherita(True))}")
    print(f"- Pepperoni 🍕 : {str(Pepperoni(True))}")
    print(f"- Hawaiian 🍍 : {str(Hawaiian(True))}")


def log(tag: str) -> Callable:
    """Параметрический декоратор
    Выводит имя функции и время выполнения
    """

    def wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return tag.format(func.__name__, result)

        return inner_wrapper

    return wrapper


@log("👨‍🍳 {} - приготовили за {} с")
def bake(pizza) -> int:
    """ Готовит пиццу """
    count = random.randint(1, 15)
    return count


@log("🚚 {} - доставили за {} с")
def deliver(pizza) -> int:
    """ Доставка пиццы """
    count = random.randint(5, 30)
    return count


@log("🏠 {} - забрали за {} с")
def pickup(pizza) -> int:
    """ Самовывоз пиццы """
    count = random.randint(8, 60)
    return count


class BasePizza:
    """ Базовый класс пицц """

    def __init__(self, is_large):
        self.is_large = is_large
        self.dict_ingredients = {"tomato_sauce": 40, "mozzarella": 150}

    def dicts(self) -> Dict:
        """ Выводит словарь пицц"""
        return self.dict_ingredients

    def __eq__(self, other) -> bool:
        """ Сравнение пицц """

        return (self.is_large == other.is_large) & (self.dicts() == other.dicts())

    def __str__(self) -> str:
        output = ", ".join(
            [key + ": " + str(value) for key, value in self.dict_ingredients.items()]
        )
        return output


class Margherita(BasePizza):
    """ Рецепт пиццы Маргариты """

    def __init__(self, is_large):
        super().__init__(is_large)
        self.dict_ingredients["tomato_sauce"] = 60
        self.dict_ingredients["tomatoes"] = 50


class Pepperoni(BasePizza):
    """ Рецепт пиццы Пепперони """

    def __init__(self, is_large):
        super().__init__(is_large)
        self.dict_ingredients["pepperoni"] = 170


class Hawaiian(BasePizza):
    """ Рецепт Гавайской пиццы """

    def __init__(self, is_large):
        super().__init__(is_large)
        self.dict_ingredients["chicken"] = 100
        self.dict_ingredients["pineapples"] = 90


if __name__ == "__main__":
    cli()
