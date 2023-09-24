import unittest
from busfee import *

class BlackBoxTesting(unittest.TestCase):
    def test1(self):
        self.assertEqual(busTicket(ticket_type=1, age=30), (1, 210))
        return
    
    def test2(self):
        self.assertEqual(busTicket(1, 70), (1, 0))
        return
    
    def test3(self):
        self.assertEqual(busTicket(1, 30), (1, 0))
        return

    def test4(self):
        self.assertEqual(busTicket(1, 30), (1, 10))
        return

    def test5(self):
        self.assertEqual(busTicket(1, 30), (1, 30))
        return    

if __name__ == '__main__':
    unittest.main(verbosity=2)