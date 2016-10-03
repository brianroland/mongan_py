# 2016-10-03: I like to return a data-only class containing a field indicating algorithm success
#
#


class BinarySearchResult(object):
    def __init__(self, success, index):
        self.success = success
        self.index = index


def binary_search(value, A, p, q):

    if q-p <= 0:
        return BinarySearchResult(False, 0)
    else:
        m = p + (q-p)/2                             # integer division

        if value == A[m]:
            return BinarySearchResult(True, m)
        elif value < A[m]:
            return binary_search(value, A, p, m)
        else:
            return binary_search(value, A, p+1, q)