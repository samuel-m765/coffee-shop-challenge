from customer import Customer
from coffee import Coffee

cust1 = Customer("Alice")
cust2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

cust1.create_order(coffee1, 3.5)
cust1.create_order(coffee2, 4.0)
cust2.create_order(coffee1, 5.0)

print(cust1.coffees())  
print(coffee1.customers())  
print(coffee1.num_orders())  
print(coffee1.average_price())  
print(Customer.most_aficionado(coffee1))  
