from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review, Base

# Replace 'your_module_name' with the actual name of the module where your SQLAlchemy code is located.

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurbase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Restaurant, Customer, and Review
restaurant1 = Restaurant(name='Restaurant 1', price=3)
restaurant2 = Restaurant(name='Restaurant 2', price=4)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')
review1 = Review(star_rating=4)
review2 = Review(star_rating=5)

# Add instances to the session and commit to the database
session.add(restaurant1)
session.add(restaurant2)
session.add(customer1)
session.add(customer2)
session.add(review1)
session.add(review2)
session.commit()

# Test class methods

# Example for Restaurant class method
fanciest_restaurant = Restaurant.restaurant_fanciest(session)
print(f"The fanciest restaurant is: {fanciest_restaurant.name}")



# Example for Restaurant instance method (getting all reviews)
all_reviews_for_restaurant2 = restaurant2.restaurant_all_reviews()
for review_sentence in all_reviews_for_restaurant2:
    print(review_sentence)

print(restaurant1.restaurant_reviews())
# Close the session
session.close()
