from random import choice
from string import ascii_letters, digits, punctuation, whitespace
from urllib.parse import urlparse

from . import app
from .models import URLMap


def get_unique_short_id():
    random_string = ""
    for _ in range(app.config['AUTOGENERATION_LENGTH']):
        random_string += choice(ascii_letters + digits)
    if URLMap.query.filter_by(short=random_string).first() is not None:
        get_unique_short_id()
    return random_string


def check_correct_url(url):
    return (urlparse(url).scheme and urlparse(url).netloc)


def check_correct_custom_id(custom_id):
    if len(custom_id) > app.config['MAX_SHORT_URL_LENGTH']:
        return False
    if any(char in set(whitespace) for char in custom_id):
        return False
    if any(char in set(punctuation) for char in custom_id):
        return False
    if any(char in set(ascii_letters) for char in custom_id):
        return True
    return False
