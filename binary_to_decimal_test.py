import unittest
from binary_to_decimal import binary_to_decimal
class TestBinaryToDecimal(unittest.TestCase):

    def test_1(self):
        resultado = binary_to_decimal(1010)
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = binary_to_decimal(1111011)
        self.assertEqual(resultado, 123)

    def test_3(self):
        resultado = binary_to_decimal(110010000)
        self.assertEqual(resultado, 400)

    def test_4(self):
        resultado = binary_to_decimal(1000100100)
        self.assertEqual(resultado, 548)


if __name__ == '__main__':
    unittest.main()