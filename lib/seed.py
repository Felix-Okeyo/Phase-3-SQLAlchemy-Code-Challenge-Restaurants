
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
            price =
        )

    
