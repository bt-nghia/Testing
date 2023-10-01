import unittest
from busfee2 import *

class BranchConverage(unittest.TestCase):
    # path 1
    def test1(self):
        self.assertRaises(ValueError, busTicketDiscount(4, True), 'invalid age or ticket_type')
        return
    
    # path 2
    def test2(self):
        self.assertEqual(busTicketDiscount(1, True), (1, 10))
        return
    
    # path 3
    def test3(self):
        self.assertEqual(busTicketDiscount(1, False), (1, 50))
        return
    
    # path 4
    def test4(self):
        self.assertEqual(busTicketDiscount(2, True), (2, 0))
        return

    # path 5
    def test5(self):
        self.assertEqual(busTicketDiscount(2, False), (2, 30))
        return    
    
    # path 6
    def test6(self):
        self.assertEqual(busTicketDiscount(3, True), (3, 0))
        return  

    # path 7
    def test7(self):
        self.assertEqual(busTicketDiscount(3, False), (3, 10))
        return
    
if __name__ == '__main__':
    unittest.main(verbosity=2)