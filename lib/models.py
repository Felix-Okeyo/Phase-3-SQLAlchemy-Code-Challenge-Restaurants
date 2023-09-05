# Import necessary SQLAlchemy modules
from sqlalchemy import create_engine, inspect
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///restaurbase.db')
inspector = inspect(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define a many-to-many relationship table between restaurants and customers
restaurant_customer = Table(
    'restaurants_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

# Define the Restaurant class with attributes and relationships
class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    
    customers = relationship('Customer', secondary=restaurant_customer, back_populates='restaurants')
    reviews = relationship('Review', back_populates='restaurant', cascade='all, delete-orphan')
    
    # Return a collection of reviews associated with the restaurant 
    def restaurant_reviews(self):
        return self.reviews
    
    # Return a collection of all customers who reviewed the restaurant
    def restaurant_customers(self):
        return self.customers 
    
    # This method returns one restaurant instance with the highest price
    @classmethod
    def restaurant_fanciest(cls, ):
        return session.query(cls).order_by(cls.price.desc()).first()
    
    # This should return a list of strings with all the reviews for this restaurant
    def restaurant_all_reviews(self):
        restaurant_review = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [review.review_full_review() for review in restaurant_review]

    def __repr__(self):
        return f'Restaurant (id={self.id}, ' + \
            f'name = {self.name}, ' + \
            f'price = {self.price})'

# Define the Customer class with attributes and relationships
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    
    restaurants = relationship('Restaurant', secondary=restaurant_customer, back_populates='customers')
    reviews = relationship('Review', back_populates='customer', cascade='all, delete-orphan')
    
    # Return a collection of reviews left by a customer 
    def customer_reviews(self):
        return self.reviews 
    
    # Return a collection of restaurants the customer has reviewed 
    def customer_restaurants(self):
        return self.restaurants 
    
    # Return customer full name in a string that is concatenated
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    # Allow the customer to add a new review of a restaurant given a restaurant's id
    def customer_add_review(self, restaurant, rating):
        # Create a new review by using the Review class attributes 
        review = Review(
            star_rating=rating, 
            restaurant_id=restaurant.id,
            customer_id=self.id 
        )
        # Append the review to the reviews list in the customer's reviews 
        self.reviews.append(review)
    
    # Delete reviews for a specific restaurant
    def customer_delete_reviews(self, restaurant):
        for review in self.reviews:
            if review.restaurant_id == restaurant.id:
                session.delete(review) # Delete the review from the database
                self.reviews.remove(review) # Remove the review from the customer's reviews list
        
        session.commit() # Commit the changes to the database session
         
    def __repr__(self):
        return f'Customer (id={self.id}),' +\
            f'name = {self.first_name},' +\
            f'price = {self.last_name})'

# Define the Review class with attributes and relationships
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    
    restaurant = relationship ('Restaurant', back_populates= 'reviews' )
    customer = relationship ('Customer', back_populates= 'reviews')
    # Return the customer instance associated with the review 
    
    def review_customer(self):
        return self.customer 
    
    # Return restaurant instance associated with the review
    
    def review_restaurant(self):
        return self.restaurant
        
    # Return a string with the full review information
    def review_full_review(self):
        return f'Review for {self.review_restaurant().name} by {self.review_customer().full_name()}: {self.star_rating} stars'    
    
    def __repr__(self):
        return f'Review (id={self.id}, ' +\
            f'star rating given = {self.star_rating}, ' +\
            f'restaurant id ={self.restaurant_id})'

# Create the database tables based on the defined models
Base.metadata.create_all(engine)
