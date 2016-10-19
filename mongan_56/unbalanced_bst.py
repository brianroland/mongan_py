import mongan_54.lowest_common_ancestor


def is_left_child(node):

    return (node.parent is not None) and (node.parent.left is node)


def is_right_child(node):

    return (node.parent is not None) and (node.parent.right is node)


def right_rotate_bst(root):

    #these are the addresses of the objects we'll modify
    old_root = root
    old_left = root.left
    old_left_right = root.left.right

    #connect up new root
    if is_left_child(old_root):
        old_root.parent.left = old_left
        old_left.parent = old_root.parent

    elif is_right_child(old_root):
        old_root.parent.right = old_left
        old_left.parent = old_root.parent

    else:
        old_left.parent = None

    #connect old_root as right child of old_left
    old_left.right = old_root
    old_root.parent = old_left

    #connect old_left_right as left child of old_root
    old_root.left = old_left_right
    old_left_right.parent = old_root
