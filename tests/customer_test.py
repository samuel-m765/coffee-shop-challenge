import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  
        with self.assertRaises(ValueError):
            Customer("a" * 16)  
        self.assertEqual(Customer("Alice").name, "Alice")

    def test_create_order_and_coffees(self):
        c = Customer("Alice")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        c.create_order(coffee1, 4.5)
        c.create_order(coffee2, 5.0)
        self.assertEqual(len(c.orders()), 2)
        self.assertIn(coffee1, c.coffees())

if __name__ == '__main__':
    unittest.main()
