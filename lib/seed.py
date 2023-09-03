
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restaurbase.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    
