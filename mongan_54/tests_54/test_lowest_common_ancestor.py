import unittest
from mongan_54.lowest_common_ancestor import *

class TestLowestCommonAncestor(unittest.TestCase):

    def test_hello_world(self):
        print 'test_hello_world: beg'
        print 'test_hello_world: end'

    def test_node(self):
        node = Node(0)
        print "node.value={0:d}".format(node.value)

    def test_three_node_tree(self):
        print 'test_lowest_common_ancestor: beg'

        a = Node(0)
        b = Node(1)
        c = Node(2)

        a.left = b
        a.right = c
        b.parent = a
        c.parent = a

        out = lowest_common_ancestor(b, c)

        self.assertEqual(out.value,a.value)
        print "ancestor has value={0:d}".format(out.value)

        print 'test_lowest_common_ancestor: end'

    def test_seven_node_tree(self):
        print 'test_seven_node_tree: beg'

        a = Node(80)
        b = Node(40)
        c = Node(120)
        d = Node(20)
        e = Node(60)
        h = Node(10)
        i = Node(30)

        a.left = b
        a.right = c
        b.parent = a
        c.parent = a

        b.left = d
        d.parent = b

        b.right = e
        e.parent = b

        h.parent = d
        d.left = h
        i.parent = d
        d.right = i

        out = lowest_common_ancestor(h, e)

        print "ancestor has value={0:d}".format(out.value)
        self.assertEqual(out.value, b.value)

        print 'test_seven_node_tree: end'

    def test_seven_node_tree_again(self):
        print 'test_seven_node_tree_again: beg'

        a = Node(80)
        b = Node(40)
        c = Node(120)
        d = Node(20)
        e = Node(60)
        h = Node(10)
        i = Node(30)

        a.left = b
        a.right = c
        b.parent = a
        c.parent = a

        b.left = d
        d.parent = b

        b.right = e
        e.parent = b

        h.parent = d
        d.left = h
        i.parent = d
        d.right = i

        out = lowest_common_ancestor(h, c)

        print "ancestor has value={0:d}".format(out.value)
        self.assertEqual(out.value, a.value)

        print 'test_seven_node_tree_again: end'