#Auto:达实泽林
#Creat Time:2021/12/23 15:38
#Creat Function:unittest框架
#Edit Auto:
#Edit Time:
#Edit Function:

import unittest

class UnitTest(unittest.TestCase):

    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')

    @classmethod
    def setUpClass(self):
        print('setUpClass\n')

    @classmethod
    def tearDownClass(self):
        print('tearDownClass')

    def test_001(self):
        print('test_001')
    def test_002(self):
        print('test_002')

if __name__ == '__main__':
    unittest.main()