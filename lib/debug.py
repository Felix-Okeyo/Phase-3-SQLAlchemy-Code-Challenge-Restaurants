
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restaurbase.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # import ipdb; ipdb.set_trace()
review1=session.query(Review).filter_by(id=2).first()
print(review1.review_customer())
print(review1.review_restaurant())
print(review1.review_full_review())

restaurant1 = session.query(Restaurant).filter_by(id=3).first()
print(restaurant1.restaurant_reviews())
print(restaurant1.restaurant_customers())
print(restaurant1.restaurant_all_reviews())


print(Restaurant.restaurant_fanciest())