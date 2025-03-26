import unittest
from back13_1 import sort_numbers 

class TestSortNumbers(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(sort_numbers([]), [])
        
    def test_sort_already_sorted(self):
        self.assertEqual(sort_numbers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
    def test_sort_reverse_order(self):
        self.assertEqual(sort_numbers([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    def test_sort_random_order(self):
        self.assertEqual(sort_numbers([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])
        
    def test_sort_negative_numbers(self):
        self.assertEqual(sort_numbers([-5, -3, -1, -4, -2]), [-5, -4, -3, -2, -1])
        
    def test_sort_mixed_numbers(self):
        self.assertEqual(sort_numbers([-3, 2, 0, -5, 1, 4]), [-5, -3, 0, 1, 2, 4])

if __name__ == "__main__":
    unittest.main()