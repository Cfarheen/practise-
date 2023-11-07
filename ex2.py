import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(6, 5), 11)  # This test will pass with the original code.

    def test_add_negative_numbers(self):
        self.assertEqual(add(-6, -5), -10)  # This test is intentionally failing.

if __name__ == '__main__':
    unittest.main()
