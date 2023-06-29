from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import (
    check_correct_custom_id,
    check_correct_url,
    get_unique_short_id
)


@app.route('/api/id/', methods=['POST'])
def add_new_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
        if not data['custom_id']:
            raise InvalidAPIUsage(
                'Произошла ошибка, '
                'попробуйте ввести свой вариант короткой ссылки \"custom_id\" '
                'или зайти позже.'
            )
    if not check_correct_custom_id(data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if not check_correct_url(data['url']):
        raise InvalidAPIUsage('Некорректная ссылка, проверьте ссылку!')
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:custom_id>/', methods=['GET'])
def get_url(custom_id):
    url = URLMap.query.filter_by(short=custom_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK
