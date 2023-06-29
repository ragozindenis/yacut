from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import check_correct_url, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short_new_url = form.custom_id.data
        original_url = form.original_link.data
        if not check_correct_url(original_url):
            flash('Некорректная ссылка, проверьте ссылку!', 'false_url')
            return render_template('index.html', form=form)
        if not short_new_url:
            short_new_url = get_unique_short_id()
            if not short_new_url:
                flash(
                    (
                        'Произошла ошибка, '
                        'попробуйте ввести свой вариант короткой ссылки '
                        'или зайти позже.'
                    ),
                    'max_call_stack'
                )
                return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=short_new_url).first() is not None:
            flash(f'Имя {short_new_url} уже занято!', 'exist_url')
            return render_template('index.html', form=form)
        url = URLMap(
            original=form.original_link.data,
            short=short_new_url
        )
        db.session.add(url)
        db.session.commit()
        flash(url.short, 'new_short_url')
        context = {'form': form, 'url': url}
        return render_template('index.html', **context)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def url_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
