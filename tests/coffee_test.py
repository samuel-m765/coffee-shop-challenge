import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    
    def test_name_validation(self):
        
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")
        
        
        with self.assertRaises(ValueError):
            Coffee("Esp")  
    
        with self.assertRaises(AttributeError):
            coffee.name = "Cappuccino"

    def test_num_orders(self):
        coffee = Coffee("Latte")
        cust1 = Customer("Alice")
        cust2 = Customer("Bob")
        
        self.assertEqual(coffee.num_orders(), 0)
    
        cust1.create_order(coffee, 3.5)
        cust2.create_order(coffee, 4.0)
        
        
        self.assertEqual(coffee.num_orders(), 2)

    def test_average_price(self):
        coffee = Coffee("Espresso")
        cust1 = Customer("Alice")
        cust2 = Customer("Bob")
        

        self.assertEqual(coffee.average_price(), 0.0)
        
        cust1.create_order(coffee, 5.0)
        cust2.create_order(coffee, 6.0)
        
        
        self.assertEqual(coffee.average_price(), 5.5)

    def test_customers(self):
        coffee = Coffee("Latte")
        cust1 = Customer("Alice")
        cust2 = Customer("Bob")
        
    
        cust1.create_order(coffee, 3.5)
        cust2.create_order(coffee, 4.0)
    
        customers = coffee.customers()
        self.assertIn(cust1, customers)
        self.assertIn(cust2, customers)

if __name__ == '__main__':
    unittest.main()
