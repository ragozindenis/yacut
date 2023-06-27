from datetime import datetime
from urllib import parse

from flask import request

from yacut import app, db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        url_root = request.url_root
        return dict(
            url = self.original,
            short_link = parse.urljoin(url_root, self.short)
        )

    def from_dict(self, data):
        for field_model, field_api in app.config['FIELDS_API'].items():
            if field_api in data:
                setattr(self, field_model, data[field_api])
