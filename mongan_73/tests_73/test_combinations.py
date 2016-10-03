import unittest
from mongan_73.combinations import *

class TestCombinations(unittest.TestCase):

    def test_hello_world(self):
        print 'test_hello_world: beg'
        print 'test_hello_world: end'

    def test_case_0(self):
        print 'test_case_0: beg'
        print_combinations_recursive_top('a')
        print 'test_case_0: end'

    def test_case_1(self):
        print 'test_case_1: beg'
        print_combinations_recursive_top('aa')
        print 'test_case_1: end'

    def test_case_2(self):
        print 'test_case_2: beg'
        print_combinations_recursive_top('hat')
        print 'test_case_2: end'