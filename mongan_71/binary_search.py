#
#
#

class BinarySearchResult(object):
    def __init__(self, success, index):
        self.success = success
        self.index = index

def floor(s):

    return int(s - s % 1)

def binary_search(value, A, p, q):

    if q-p <=0:
        return BinarySearchResult(False,0)
    else:
        m = p + floor( (q-p)/2 )

        if value==A[m]:
            return BinarySearchResult(True, m)
        elif value < A[m]:
            return binary_search(value, A, p, m)
        else:
            return binary_search(value, A, p+1, q)