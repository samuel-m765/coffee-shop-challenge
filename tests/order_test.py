import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):

    def test_initialization(self):
        # Create instances of Customer and Coffee
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        
        # Create an order for the customer and coffee
        order = Order(customer, coffee, 4.5)
        
        # Test that the order is initialized correctly
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)
        
        # Ensure that the price is immutable
        with self.assertRaises(AttributeError):
            order.price = 5.0
    
    def test_order_relationship(self):
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        
        # Create an order
        order = Order(customer, coffee, 5.0)
        
        # Ensure that the order belongs to the correct customer and coffee
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)

    def test_order_customer_relationship(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Latte")
        
        # Create orders for the customers
        customer1.create_order(coffee, 3.5)
        customer2.create_order(coffee, 4.0)
        
        # Ensure that both customers are associated with the coffee
        customers = coffee.customers()
        self.assertIn(customer1, customers)
        self.assertIn(customer2, customers)

if __name__ == '__main__':
    unittest.main()
