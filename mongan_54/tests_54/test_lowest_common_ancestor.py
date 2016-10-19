import unittest
from mongan_54.lowest_common_ancestor import *

class TestLowestCommonAncestor(unittest.TestCase):

    def test_hello_world(self):
        print 'test_hello_world: beg'
        print 'test_hello_world: end'

    def test_node(self):
        node = Node(0)
        print "node.value={0:d}".format(node.value)