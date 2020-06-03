import unittest
import intro

class TestAss1(unittest.TestCase):

    def test_permute3Chars(self):
        self.assertEqual(intro.permute('ABC'),['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'])

    def test_permute2Chars(self):
        self.assertEqual(intro.permute('AB'),['AB', 'BA'])

    def test_permute1Chars(self):
        self.assertEqual(intro.permute('A'),['A'])


if __name__ == "__main__":
        unittest.main()


