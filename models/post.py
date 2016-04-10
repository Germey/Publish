# -*- coding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    id = sa.Column(sa.Integer, primary_key = True, autoincrement = True)
    title = sa.Column(sa.String(64))
    content = sa.Column(sa.Text)
    username = sa.Column(sa.String)

    def __init__(self, title=title, content=content, username=username):
        self.title = title
        self.content = content
        self.username = username


    def __repr__(self):
        return '<Post %s> [Content %s]' % (self.title, self.content)
