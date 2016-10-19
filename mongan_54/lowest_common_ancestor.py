


class Node(object):

    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


def on_same_side(smaller, larger, target):
    return (smaller.value <= target.value) == (larger.value <= target.value)


def split_by(smaller, larger, target):
    return (smaller.value <= target.value) and (larger.value > target.value)


def lowest_common_ancestor(node_x, node_y):
    print 'LowestCommonAncestor: beg'

    assert node_x is not None
    assert node_y is not None

    smaller = node_x
    larger = node_y
    if node_y.value < node_x.value:
        smaller = node_y
        larger = node_x

    current = smaller.parent                    #know that smaller has a parent
    parent = smaller.parent.parent              #this could be null

    while True:

        if parent is None:
            return current

        elif split_by(smaller, larger, current) and on_same_side(smaller, larger, parent):
            return current

        else:
            current = parent
            parent = current.parent



    print 'LowestCommonAncestor: end'
