from sqlalchemy import create_engine, inspect
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref, session
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
    
    # return a collection of reviews associated with the restaurant 
    def restaurant_reviews(self):
        return self.reviews
    
    #return a collection of all customers who reviewed the restaurant
    def restaurant_customers(self):
        return self.customers 
    
    #This method returns one restaurant instance with the highest price
    @classmethod
    def restaurant_fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()
    
    #This should return an list of strings with all the reviews for this restaurant
    #"Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
    def restaurant_all_reviews(self):
        restaurant_review = session.query(Review).order_by(restaurant_id=self.id).all()
        return[review.review_full_review() for review in restaurant_review]

   
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
    
    #return a collection of reviews left by a customer 
    def customer_reviews(self):
        return self.reviews 
    #return a colletion of restaurants the customer has reviewed 
    def customer_restaurants(self):
        return self.restaurants 
    
    # return customer full bame in a string that is concatenated
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
   #should allow the customer to add a new review of a restaurant given a restaurant's id
    def customer_add_review(self, restaurant, rating):
        #create a new review by using the Review class attributes 
        review = Review(
        star_rating = rating, 
        rastaurant_id = restaurant.id,
        customer_id = self.id 
        )
        # append the review to the reviews list in the customer's reviews 
        self.reviews.append(review)
    
    def customer_delete_reviews(self,restaurant, session):
        for review in self.reviews:
            if review.restaurant_id == restaurant.id:
                session.delete(review) # Delete the review from the database
                self.reviews.remove(review) # Remove the review from the customer's reviews list
        
        session.commit() # Commit the changes to the database session
         
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
    
    # restaurant = relationship('Restaurant', back_populates = 'reviews')
    # customer = relationship('Customer', back_populates ='reviews')
    # return the customer instance associated with the review 
    # @property
    def review_customer(self):
        return self.customer_id 
    # return restaurant instance associated with the review
    # @property 
    def review_restaurant(self):
        return self.restaurant_id
        
    def review_full_review(self):
        return f'Review for {self.review_restaurant().name} by {self.review_customer().full_name()}: {self.star_rating} stars'    
    
    def __repr__(self):
        return f'Review (id={self.id}, ' +\
            f'star rating given = {self.star_rating}, ' +\
            f'restaurant id ={self.restaurant_id})'

Base.metadata.create_all(engine)


# customer = session.query(Customer).filter_by(id=1).first()

