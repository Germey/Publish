# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/publish')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
db = DBSession()