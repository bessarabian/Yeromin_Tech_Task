import unittest
from checker import check_password

class TestChecker(unittest.TestCase):

    def setUp(self):
        self.check_password = check_password

    def test_check_password(self):
        self.assertEqual(self.check_password("qwertWEQ#ddjyRw#"), False) # no digits
        self.assertEqual(self.check_password('=|ib9}5nb]pI1k/9'), True) # good password
        self.assertEqual(self.check_password('onlylowercasepasswordcheck'), False) # only lowercase
        self.assertEqual(self.check_password('ONLYUPPERCASE@@@@@123'), False) # good password but no lowercase
        self.assertEqual(self.check_password(12344123), False) # only digits

if __name__ == '__main__':
    unittest.main()