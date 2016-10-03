
from mongan_71.binary_search import *
import unittest

class TestBinarySearch(unittest.TestCase):

    def test_hello_world(self):
        print 'test_hello_world: beg'
        self.assertEqual('foo'.upper(), 'FOO')
        print 'test_hello_world: end'

    def test_case_0(self):
        print 'test_case_0'
        A = list()
        out = binary_search(8, A, 0,len(A))
        self.assertEquals(out.success, False)
        print 'test_case_0'

    def test_case_1(self):
        print 'test_case_1'
        A = list([8])
        out = binary_search(8, A, 0,len(A))
        self.assertEquals(out.success, True)
        self.assertEquals(out.index, 0)
        print 'test_case_1'

    def test_case_2(self):
        print 'test_case_1'
        A = list([9,11])
        out = binary_search(11, A, 0, len(A))
        self.assertEquals(out.success, True)
        self.assertEquals(out.index, 1)
        print 'test_case_2'


if __name__ == '__main__':
    unittest.main()