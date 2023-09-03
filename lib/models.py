from sqlalchemy import create_engine, inspect
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurbase.db')
inspector = inspect(engine)

Base = declarative_base()

restaurant_customer = Table(
    'restaurants_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key = True),
    Column('customer_id', ForeignKey('customers.id'), primary_key = True),
    extend_existing = True,
)

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())
    
    customers = relationship('Customer', secondary = restaurant_customer, back_populates = 'restaurants')
    reviews = relationship ('Review', backref = backref('restaurant'), cascade = 'all, delete-orphan')
    
    def __repr__(self):
        return f'Restaurant (id={self.id}, ' + \
            f'name = {self.name}, ' + \
            f'price = {self.price})'

    

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    
    restaurants = relationship('Restaurant', secondary = restaurant_customer, back_populates = 'customers')
    reviews = relationship('Review', backref = backref('customer'), cascade = 'all, delete-orphan')
    
    def __repr__(self):
        return f'Customer (id={self.id}),' +\
            f'name = {self.first_name},' +\
            f'price = {self.last_name})'
    
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer(), primary_key = True)
    star_rating = Column(Integer())
    
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    
    def __repr__(self):
        return f'Review (id={self.id}, ' +\
            f'star rating given = {self.star_rating}, ' +\
            f'restaurant id ={self.restaurant_id})'

Base.metadata.create_all(engine)