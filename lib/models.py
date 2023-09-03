from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurbase.db')

Base = declarative_base()



class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())
    

class Customer(Base):
    __tablename__ = 'Customers'
    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    
    
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer(), primary_key = True)
    star_rating = Column(Integer())
    