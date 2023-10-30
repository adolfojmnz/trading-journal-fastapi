import random

from app.tests.utils.common import generate_random_string


def generate_random_symbol():
    random_symbol = generate_random_string(length=3, uppercase=True)
    return random_symbol


def generate_random_name():
    random_name = generate_random_string(length=6)
    return random_name


def generate_random_dicimal_position():
    random_number = random.randint(2, 5)
    return random_number


def generate_random_asset():
    symbol = generate_random_symbol()
    name = generate_random_name()
    decimal_position = generate_random_dicimal_position()

    asset = {
        "symbol": symbol,
        "name": name,
        "pip_on_decimal": decimal_position,
    }

    return asset
