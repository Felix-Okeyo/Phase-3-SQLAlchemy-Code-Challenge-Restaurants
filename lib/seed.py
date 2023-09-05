# Import necessary modules
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer  # Import your SQLAlchemy models

if __name__ == '__main__':
    # Create a SQLAlchemy database engine
    engine = create_engine('sqlite:///restaurbase.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Uncomment and use these lines to clear existing data in the database
    # session.query(Restaurant).delete()
    # session.query(Review).delete()
    # session.query(Customer).delete()
    
    fake = Faker()
    
    names = ['Kempinski', 'Sarova', 'Intercontinental', 'Sarova', 
             'Serena', 'The One', 'Park View', 'Ole Sereni', 'Weston', 
             'Radisson Blue', 'Hemingways', 'Sankara', 'The Tribe', 'The Boma']
    
    restaurants = []
    for item in range(50):
        restaurant = Restaurant(
            name=random.choice(names),
            price=random.randint(200, 500)
        )
        
        # Add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()
        
        restaurants.append(restaurant)
        
    customers = []
    for i in range(50):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        session.add(customer)
        session.commit()
        
        customers.append(customer)
        
    reviews = []
    for restaurant in restaurants:
        for item in range(random.randint(1, 5)):
            customer = random.choice(customers)
            if restaurant not in customer.restaurants:
                customer.restaurants.append(restaurant)
                session.add(customer)
                session.commit()
            
            review = Review(
                star_rating=random.randint(0, 10),
                restaurant_id=restaurant.id,
                customer_id=customer.id,
            )
            reviews.append(review)
    
    # Use bulk_save_objects to efficiently insert reviews into the database
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
