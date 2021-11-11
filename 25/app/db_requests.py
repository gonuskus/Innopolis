from datetime import datetime

from app import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from .Exceptions import *


class Bases:
    def create_user(self, new_user):
        try:
            session.add(new_user)
            session.commit()
        except IntegrityError:
            session.rollback()
            raise Exception_400('ERROR: Запись с таким именем уже создана')
        except:
            session.rollback()
            raise Exception_500('ERROR rollback: Что то пошло не так при создании записи')
        new_search_result = self.search_user(new_user.__tablename__, userid=new_user.id)
        if not new_search_result:
            raise Exception_500('ERROR new_search_result: Что то пошло не так при создании записи')
        else:
            return new_search_result

    def search_user(self, table, userid=None):
        filters = ()
        if userid is not None:
            new_part = (f"id={userid}",)
            filters += new_part

        if table == 'clients':
            user_data = session.query(Clients).filter(text(*filters)).all()
        elif table == 'drivers':
            user_data = session.query(Drivers).filter(text(*filters)).all()
        else:
            raise Exception_500('ERROR search_user: Что то пошло не так при поиске записи')
        return user_data

    def delete_user(self, existed_user):
        search_result = self.search_user(existed_user.__tablename__, existed_user.id)
        if not search_result:
            raise Exception_404('ERROR: Пользователь НЕ существует')
        else:
            try:
                if existed_user.__tablename__ == 'clients':
                    session.query(Clients).filter_by(id=existed_user.id).delete()
                elif existed_user.__tablename__ == 'drivers':
                    session.query(Drivers).filter_by(id=existed_user.id).delete()
                else:
                    raise Exception_500('ERROR: Что то пошло не так при удалении записи')
                session.commit()
                return
            except:
                session.rollback()
                raise Exception_500('ERROR: Что то пошло не так при удалении записи')


'''    def update_user(self, existed_user):
        print('update_user')
        self.delete_user(existed_user.username)
        self.create_user(existed_user)'''


class Clients(Base):
    __tablename__ = 'clients'  # имя таблицы
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, comment="Идентификатор учетной записи")
    name = Column(String, nullable=False, unique=True, comment="Логин")
    is_vip = Column(Boolean, nullable=False, comment="Важность клиента")

    def __repr__(self):
        return "<Clients(id=%s, name='%s', is_vip='%s')>" % (self.id, self.name, self.is_vip)


class Drivers(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, comment="Идентификатор учетной записи")
    name = Column(String, nullable=False, unique=True, comment="Логин")
    car = Column(String, nullable=False, comment="Марка автомобиля")

    def __repr__(self):
        return "<Drivers(id=%s, name='%s', car='%s')>" % (self.id, self.name, self.car)


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, comment="Id заказа")
    address_from = Column(String, nullable=False, comment="Адрес отправки")
    address_to = Column(String, nullable=False, comment="Адрес назначения")
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False, comment="Id клиента")
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False, comment="Id клиента")
    date_created = Column(TIMESTAMP, nullable=False, comment="Дата создания заказа")
    status = Column(String, nullable=False, comment="Статус заказа")
    drivers = relationship("Drivers", foreign_keys=[driver_id])

    def __repr__(self):
        return f"<(id={self.id}, status={self.status}, client_id={self.client_id}, driver_id={self.driver_id})>"

    def create_order(self, client_id, driver_id, address_from, address_to):
        new_order = Orders(client_id=client_id,
                           driver_id=driver_id,
                           address_from=address_from,
                           address_to=address_to,
                           date_created=datetime.now(),
                           status='not_accepted'
                           )
        session.add(new_order)
        session.commit()
        new_search_result = self.search_order(id_order=new_order.id)
        if not new_search_result:
            raise Exception_500('ERROR: Что то пошло не так при создании заказа')
        return new_search_result

    def search_order(self, id_order):
        search_result = session.query(Orders).filter(text(f"id={id_order}")).all()
        if not search_result:
            raise Exception_404('ERROR: Заказ с такими данными не найден')
        return search_result

    def update_order(self, id_order, new_client_id=None, new_driver_id=None, new_status=None, new_address_from=None,
                     new_address_to=None, new_date_created=None):
        search_result = self.search_order(id_order)

        filters = {}
        if search_result[0].status == 'not_accepted' and (
                new_client_id is not None or new_driver_id is not None or new_date_created is not None):
            if new_client_id is not None:
                filters["client_id"] = new_client_id
            if new_driver_id is not None:
                filters["driver_id"] = new_driver_id
            if new_date_created is not None:
                filters['date_created'] = new_date_created

        if new_address_from is not None:
            filters["address_from"] = new_address_from
        if new_address_to is not None:
            filters["address_to"] = new_address_to
        if new_status is not None and self.validate_change_status(search_result[0].status, new_status):
            filters["status"] = new_status
        elif not self.validate_change_status(search_result[0].status, new_status):
            raise Exception_500(f"ERROR: Статус {search_result[0].status} нельзя сменить на {new_status}")

        session.query(Orders).filter_by(id=id_order).update(filters)
        session.commit()
        new_search_result = self.search_order(id_order=id_order)
        if not new_search_result:
            raise Exception_500('ERROR: Что то пошло не так при изменении заказа')
        return new_search_result

    def validate_change_status(self, old_status, new_status):
        if old_status == 'not_accepted':
            if new_status == 'in_progress':
                return 1
            elif new_status == 'cancelled':
                return 1
        elif old_status == 'in_progress':
            if new_status == 'done':
                return 1
            elif new_status == 'cancelled':
                return 1
        return 0


Sessions = sessionmaker(bind=engine)
session = Sessions()
