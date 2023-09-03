
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restaurbase.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.query(Customer).delete()
    
    fake = Faker()
    
    names = ['Kenmpinski', 'Sarova', 'Intercontinental', 'Sarova', 
             'Serena', 'The One', 'Park View', 'Ole Sereni', 'Weston', 
             'Radisson Blue','Hemingways', 'Sankara', 'The Tribe', 'The Boma' ]
    
    
    restaurants = []
    for item in range (50):
        restaurant = Restaurant(
            name = random.choice(names),
            price = random.randint(2000, 15000)
        )
        
        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()
        
        restaurants.append(restaurant)
        
    customers = []
    for i in range(50):
        customer = Customer(
            name = fake.name(),
        )
        session.add(customer)
        session.commit(customer)
        
        customers.append(customer)
        
        
    reviews = []
    for restaurant in restaurants:
        for item in range(random.randint(1,5)):
            customer = random.choice(customers)
            if restaurant not in customer.restaurants:
                customer.restaurants.append(restaurant)
                session.add(customer)
                session.commit()
            
            review = Review(
                star_rating = random.randint(0,10),
                restaurant_id = restaurant.id,
                customer_id = customer.id,
            )
            reviews.append(review)
    
    
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()

    
