import unittest
from mongan_72.permutations import *

class TestBinarySearch(unittest.TestCase):

    def test_hello_world(self):
        print 'test_hello_world: beg'
        self.assertEqual('foo'.upper(), 'FOO')
        print 'test_hello_world: end'

    def test_case_0(self):
        print 'test_case_0'
        word = 'a'
        print_perms_recursive_top(word)
        print 'test_case_0'

    def test_case_1(self):
        print 'test_case_1'
        word = 'add'
        print_perms_recursive_top(word)
        print 'test_case_1'

    def test_case_2(self):
        print 'test_case_2'
        word = 'hat'
        print_perms_recursive_top(word)
        print 'test_case_2'