import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Ladywell", 500.00)
        self.drink = Drink("Negroni", 7.50)

    def test_pub_has_name(self):
        self.assertEqual("The Ladywell", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500, self.pub.till)

    def test_drink_has_name(self):
        self.assertEqual("Negroni", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(7.50, self.drink.price)
    
    def test_pub_has_drink(self):
        self.pub.add_drink_to_pub(self.drink)
        self.assertEqual(1, self.pub.drink)

    

    



    

    
        