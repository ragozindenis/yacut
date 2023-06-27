from random import choice, randint
from string import ascii_letters, punctuation, whitespace
from urllib.parse import urlparse

from . import app
from .models import URLMap


def get_unique_short_id():
    random_string = ""
    for i in range(app.config['AUTOGENERATION_LENGTH']):
        number = chr(randint(48, 57))
        uppercase = chr(randint(65, 90))
        lowcase = chr(randint(97, 122))
        random_symbols = uppercase, lowcase, number
        symbol = choice(random_symbols)
        random_string += symbol
    if URLMap.query.filter_by(short=random_string).first() is not None:
        return get_unique_short_id()
    return random_string


def check_correct_url(url):
    if urlparse(url).scheme and urlparse(url).netloc:
        return True
    else:
        False


def check_correct_custom_id(custom_id):
    check_whitespace = set(whitespace)
    check_invalidcharacters= set(punctuation)
    check_letters = set(ascii_letters)
    if len(custom_id) > app.config['MAX_SHORT_URL_LENGTH']:
        return False
    elif any(char in check_whitespace for char in custom_id):
        return False
    elif any(char in check_invalidcharacters for char in custom_id):
        return False
    elif any(char in check_letters for char in custom_id):
        return True
    else:
        return False
