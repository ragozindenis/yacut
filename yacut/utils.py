from random import choice
from string import ascii_letters, digits, punctuation, whitespace
from urllib.parse import urlparse

from . import app
from .models import URLMap


def get_unique_short_id(call_stack=0):
    while call_stack < app.config['MAX_CALL_STACK']:
        random_string = ''.join(
            choice(ascii_letters + digits) for _ in range(
                app.config['AUTOGENERATION_LENGTH']
            )
        )
        if not URLMap.query.filter_by(short=random_string).first():
            return random_string
        call_stack += 1
        get_unique_short_id(call_stack)


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
