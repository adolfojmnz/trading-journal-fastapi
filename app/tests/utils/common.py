import random
import string


def generate_random_string(length, uppercase=None):
    if uppercase is True:
        letters = string.ascii_uppercase
    elif uppercase is False:
        letters = string.ascii_lowercase
    else:
        letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
