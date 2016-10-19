import unittest
from mongan_54.lowest_common_ancestor import *
from mongan_56.unbalanced_bst import *


class TestUnbalancedBST(unittest.TestCase):

    def TestHelloWorld(self):
        print 'TestHelloWorld: beg'
        print 'TestHelloWorld: end'

    def TestThreeNodeTree(self):
        print 'TestThreeNodeTree: beg'

        a = Node(80)
        b = Node(40)
        c = Node(120)
        d = Node(20)
        e = Node(60)
        f = Node(100)

        i = Node(50)
        j = Node(70)

        a.left = b
        b.parent = a
        a.right = c
        c.parent = a

        b.left = d
        d.parent = b
        b.right = e
        e.parent = b

        c.left = f
        f.parent = c

        e.left = i
        i.parent = e

        e.right = j
        j.parent = e

        right_rotate_bst(a)

        print 'TestThreeNodeTree: end'