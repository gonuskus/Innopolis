from flask import Flask
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base



app = Flask(__name__)

engine = create_engine('sqlite:///taxi.db')
Base = declarative_base()

from .db_requests import * # задаем модели которые должны в бд быть подготовлены
Base.metadata.create_all(engine)


from . import route # обозначаем url с которыми работает сервис
