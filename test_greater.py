import unittest

def true(x):
    return x>=100

class TestMultiply(unittest.TestCase):
    def test(self):
        self.assertTrue(true(101))
    
if __name__ == '__main__':
    unittest.main()
    
Ronquillo, James Wilfred
