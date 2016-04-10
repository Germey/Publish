# -*- coding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    id = sa.Column(sa.Integer, primary_key = True, autoincrement = True)
    username = sa.Column(sa.String(64))
    password = sa.Column(sa.String)

    def __init__(self, username=username, password=password):
        self.username = username
        self.password = password


    def __repr__(self):
        return '<User %s>' % (self.username)


