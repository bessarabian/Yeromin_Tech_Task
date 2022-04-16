import unittest
from checker import check_password

class TestChecker(unittest.TestCase):

    def setUp(self):
        self.check_password = check_password

    def test_check_password(self):
        self.assertEqual(self.check_password("qwertWEQ#ddjyRw#"), '- Password must contain digits\n') # no digits
        self.assertEqual(self.check_password('=|ib9}5nb]pI1k/9'), 'Your password is strong enough!') # good password
        self.assertEqual(self.check_password('ONLYUPPERCASE@@@@@123'), '- Password must contain lowercase letters\n') # good password but no lowercase

if __name__ == '__main__':
    unittest.main()