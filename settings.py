import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    FIELDS_API = ({'original': 'url', 'short': 'custom_id'})
    AUTOGENERATION_LENGTH = 6
    MAX_SHORT_URL_LENGTH = 16
