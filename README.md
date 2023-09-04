# Phase-3-SQLAlchemy-Code-Challenge-Restaurants
Restaurant and Customer Management System

This is a simple Python application that utilizes the SQLAlchemy library to manage restaurants, customers, and their reviews. It allows you to perform various operations such as adding restaurants and customers, leaving reviews, and querying restaurant data based on different criteria.
Prerequisites

Before using this application, make sure you have the following installed:

    Python (>=3.9)
    SQLAlchemy (>=1.4)
    SQLite (for the restaurbase.db)

Getting Started

    Clone this repository to your local machine:

    shell

git clone https://github.com/Felix-Okeyo/Phase-3-SQLAlchemy-Code-Challenge-Restaurants
cd restaurant-customer-management

Install the required Python packages:

shell

pip install sqlalchemy

Create the SQLite database and tables by running the create_db.py script:

shell

python seed.py

Now, you can run the main.py script to interact with the system:

shell

    python debug.py

Using the Application
Main Menu

Upon running main.py, you will be presented with a main menu with the following options:

    Manage Restaurants
    Manage Customers
    Quit

Managing Restaurants
1. Add a Restaurant

You can add a new restaurant by providing its name and price level (1-5). The restaurant's information will be saved in the database.
2. List Restaurants

This option displays a list of all restaurants, including their names and price levels.
3. Find the Fanciest Restaurant

This option retrieves the restaurant with the highest price level and displays its details.
4. Back to Main Menu

Returns to the main menu.
Managing Customers
1. Add a Customer

You can add a new customer by providing their first name and last name. The customer's information will be saved in the database.
2. List Customers

This option displays a list of all customers, including their full names.
3. Add a Review

To add a review, select a customer and a restaurant. Provide a star rating (1-5) for the review. The review will be associated with the selected customer and restaurant.
4. Delete Reviews

Select a customer and a restaurant to delete their review for that restaurant.
5. Back to Main Menu

Returns to the main menu.
Sample Code Explanation

The application is built using SQLAlchemy and includes three main classes: Restaurant, Customer, and Review. These classes are mapped to database tables and have methods to interact with the data.

    Restaurant class represents restaurants and includes methods for managing restaurant data.
    Customer class represents customers and includes methods for managing customer data and reviews.
    Review class represents reviews left by customers for restaurants.

Feel free to explore the code to understand how these classes are structured and how SQLAlchemy relationships and ORM features are used.
Contributions

Contributions are welcome! If you have any improvements or feature suggestions, please create a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy using your Restaurant and Customer Management System! If you have any questions or need further assistance, please don't hesitate to ask.