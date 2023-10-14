import unittest
from busfee3 import *

class allUser(unittest.TestCase):
    def test1(self):
        self.assertRaises(ValueError, busTicketDiscount(4, True), 'invalid age or ticket_type')
        return
    
    def test2(self):
        self.assertEqual(busTicketDiscount(1, False), (1, 50))
        return
    
    def test3(self):
        self.assertEqual(busTicketDiscount(1, False), (1, 50))
        return
    
    def test4(self):
        self.assertEqual(busTicketDiscount(2, False), (2, 30))
        return

    def test5(self):
        self.assertEqual(busTicketDiscount(3, False), (3, 10))
        return    
    
    def test6(self):
        self.assertEqual(busTicketDiscount(1, False), (1, 50))
        return  

    def test7(self):
        self.assertEqual(busTicketDiscount(1, True), (1, 10))
        return
    
    def test8(self):
        self.assertEqual(busTicketDiscount(2, False), (2, 30))
        return

    def test9(self):
        self.assertEqual(busTicketDiscount(2, True), (2, 00))
        return
    
    def test10(self):
        self.assertEqual(busTicketDiscount(3, False), (3, 10))
        return
    
    def test11(self):
        self.assertEqual(busTicketDiscount(3, True), (3, 0))
        return
    

if __name__ == '__main__':
    unittest.main(verbosity=2)