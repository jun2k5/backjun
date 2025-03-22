import unittest
from back12_2 import find_constructor  # constructor.py에서 함수를 임포트

class TestConstructor(unittest.TestCase):
    def test_constructor_found(self):
        self.assertEqual(find_constructor(216), 198)
    
    def test_constructor_not_found(self):
        self.assertEqual(find_constructor(1), 0)
    
    def test_edge_case(self):
        self.assertEqual(find_constructor(1000000), 0)  # 생성자가 없을 수 있는 큰 수

if __name__ == "__main__":
    unittest.main()