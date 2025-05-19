Coffee Shop Challenge
Overview
This project is designed to simulate a simple coffee shop system using Python classes and object-oriented programming (OOP). The system includes three core models:

Customer: Represents a customer of the coffee shop.

Coffee: Represents different types of coffee available in the shop.

Order: Represents a customer's order for a specific coffee.

The project is built to demonstrate relationships between these models, including many-to-many relationships between customers and coffee, and various aggregation methods.

Features
Customer:

Validates name (1–15 characters).

Can place orders for coffee and track their previous orders.

Coffee:

Stores coffee name (minimum 3 characters).

Tracks how many times a particular coffee has been ordered.

Calculates the average price of orders for that coffee.

Order:

Links a customer with a coffee they ordered and records the price.

Ensures that the price is within the valid range (1.0–10.0).

Aggregation & Relationships:

Customers can view all coffees they've ordered.

Coffees can see all customers who have ordered them.

Order objects track the customer and coffee associated with the order.

Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/coffee-shop-challenge.git
cd coffee-shop-challenge
Set up the Python environment:
Make sure Python 3 is installed. You can create a virtual environment using pipenv:

bash
Copy
Edit
pipenv install
pipenv shell
Install the dependencies:
If you're not using pipenv, you can install the necessary packages directly:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:
Once everything is set up, you can test the system by running debug.py or running individual test files.

Usage
Creating Instances
Here’s how you can create customers, coffee, and place orders:

python
Copy
Edit
from customer import Customer
from coffee import Coffee

# Create customers
cust1 = Customer("Alice")
cust2 = Customer("Bob")

# Create coffee options
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Customer placing orders
cust1.create_order(coffee1, 3.5)
cust2.create_order(coffee2, 4.0)
cust1.create_order(coffee2, 4.5)
Accessing Data
Once orders are placed, you can access data like so:

python
Copy
Edit
# Accessing customer's coffee orders
print(cust1.coffees())  # ['Latte', 'Espresso']

# Accessing coffee's customers
print(coffee1.customers())  # ['Alice']

# Accessing number of orders for a specific coffee
print(coffee1.num_orders())  # 2

# Accessing the average price of a specific coffee
print(coffee1.average_price())  # 3.75
Running Tests
You can run the tests using the Python unittest framework. Ensure you have all dependencies installed, then run the following command:

bash
Copy
Edit
python3 -m unittest discover -s tests
Alternatively, you can run a specific test file:

bash
Copy
Edit
python3 -m unittest tests.coffee_test
python3 -m unittest tests.order_test
python3 -m unittest tests.customer_test
This will run the respective tests for the Coffee, Order, or Customer classes.

Folder Structure
The project is organized as follows:

bash
Copy
Edit
coffee-shop-challenge/
├── customer.py          # Contains the Customer class
├── coffee.py            # Contains the Coffee class
├── order.py             # Contains the Order class
├── debug.py             # For testing the system with sample data
└── tests/               # Contains the test files
    ├── customer_test.py # Tests for the Customer class
    ├── coffee_test.py   # Tests for the Coffee class
    └── order_test.py    # Tests for the Order class
Example Test Cases
Customer Tests
Ensure name validation enforces 1–15 character length.

Verify that customers can only have orders with valid prices.

Coffee Tests
Ensure coffee names are validated (minimum 3 characters).

Test that the correct number of orders is recorded for each coffee.

Verify that the average price of coffee orders is calculated correctly.

Order Tests
Verify that orders correctly associate a customer with a coffee.

Ensure the price of an order is immutable once set.

Contributing
Feel free to fork this project, submit issues, or create pull requests to improve it!


