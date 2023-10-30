import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    username = generate_random_string(8)
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_random_user():
    username = generate_random_string(8)
    first_name = generate_random_string(6)
    last_name = generate_random_string(8)
    password = generate_random_string(10)
    email = generate_random_email()

    user = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'email': email
    }

    return user
