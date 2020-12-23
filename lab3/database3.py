import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship ,sessionmaker


DATABASE_URI = 'postgres+psycopg2://postgres:@localhost:2582/MyDatabase'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    shelf_life = Column(String,primary_key = True)
    cost = Column(Integer)
    def __init__(self,shelf_life,cost):
        self.shelf_life=shelf_life
        self.cost = cost

class Seller(Base):
    __tablename__ = 'seller'
    seller_name = Column(String,primary_key = True)
    experience = Column(String)
    cashbox = Column(Integer)
    def __init__(self,seller_name,experience,cashbox):
        self.seller_name=seller_name
        self.experience = experience
        self.cashbox = cashbox

class Shelf_life(Base):
    __tablename__ = 'shelf_life'
    date = Column(String,primary_key = True)
    valid = Column(String)
    def __init__(self,date,valid):
        self.date=date
        self.valid=valid

class Shopper(Base):
    __tablename__ = 'shopper'
    shopper_name = Column(String,primary_key = True)
    money = Column(Integer)
    search_product = Column(String)
    def __init__(self,shopper_name,money,search_product):
        self.shopper_name = shopper_name
        self.search_product = search_product
        self.money=money