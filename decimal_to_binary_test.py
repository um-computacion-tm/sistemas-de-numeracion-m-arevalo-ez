import unittest
from decimal_to_binary import decimal_to_binary
class TestDecimalToBinary(unittest.TestCase):
    
    def test_1(self):
        resultado = decimal_to_binary(1)
        self.assertEqual(resultado, "1")

    def test_2(self):
        resultado = decimal_to_binary(2)
        self.assertEqual(resultado, "10")

    def test_23(self):
        resultado = decimal_to_binary(100)
        self.assertEqual(resultado, "1100100")

    def test_4(self):
        resultado = decimal_to_binary(567)
        self.assertEqual(resultado, "1000110111")

    def test_6(self):
        resultado = decimal_to_binary(10000)
        self.assertEqual(resultado, "10011100010000")

if __name__ == "__main__":
    unittest.main() 