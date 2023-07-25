from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import time


engine = create_engine("postgresql+psycopg2://root:root@pg_db:5432/db")
Base = declarative_base()


class Menu(Base):
    __tablename__ = 'Menu'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


association_table = Table(
    'association_table',
    Base.metadata,
    Column('order_id', ForeignKey('Order.id')),
    Column('Items_id', ForeignKey('Items.id'))
)


class Order(Base):
    __tablename__ = 'Order'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    items = relationship('Items', secondary=association_table, backref='Order')


class Items(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    order = relationship('Order', secondary=association_table, backref='Items')


Base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)


