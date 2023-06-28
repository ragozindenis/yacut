from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from . import app


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(max=256)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=16),
            Regexp(
                app.config['REGEX_STRING'],
                message='Указано недопустимое имя для короткой ссылки'
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
