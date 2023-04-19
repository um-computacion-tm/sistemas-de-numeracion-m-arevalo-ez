import unittest
from decimal_to_binary import decimal_to_binary
class TestDecimalToBinary(unittest.TestCase):
    
    def test_1(self):
        resultado = decimal_to_binary(1)
        self.assertEqual(resultado, 1)

    def test_1(self):
        resultado = decimal_to_binary(2)
        self.assertEqual(resultado, 10)

if __name__ == "__main__":
    unittest.main() 