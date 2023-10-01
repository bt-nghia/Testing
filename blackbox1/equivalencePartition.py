import unittest
from busfee import *

class EquiPartition(unittest.TestCase):
    def test1(self):
        self.assertEqual(busTicketDiscount(1, True), (1, 10))
        return
    
    def test2(self):
        self.assertEqual(busTicketDiscount(3, True), (3, 0))
        return
    
    def test3(self):
        self.assertEqual(busTicketDiscount(1, False), (1, 50))
        return

    def test4(self):
        self.assertEqual(busTicketDiscount(2, False), (2, 30))
        return

if __name__ == '__main__':
    unittest.main(verbosity=2)