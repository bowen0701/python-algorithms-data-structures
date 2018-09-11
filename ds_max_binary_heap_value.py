from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MaxBinaryHeapValue(object):
    """Max Binary Heap with value implementation of Priority Queue.

    Max-heap property: A[parent(i)][0] >= A[i][0].
    """
    def __init__(self):
        self.A = [[0, 0]]
        self.size = 0

    def show(self):
        print(self.A)

    def find_max(self):
        return self.A[1]

    def max_heapify(self, i):
        """Max heapify operation.

        Complexity: log(n).
        """ 
        l = left(i)
        r = right(i)
        if l <= self.size and self.A[l][0] > self.A[i][0]:
            max_i = l
        else:
            max_i = i
        if r <= self.size and self.A[r][0] > self.A[max_i][0]:
            max_i = r
        if max_i != i:
            self.A[i], self.A[max_i] = self.A[max_i], self.A[i]
            self.max_heapify(max_i)

    def extract_max(self):
        if self.size < 1:
            raise ValueError('Heap underflow.')
        maximum = self.A[1]
        last = self.A.pop()
        self.size -= 1
        if self.size < 1:
            # The last element is maximum.
            pass
        else:
            self.A[1] = last
        self.max_heapify(1)
        return maximum

    def increase_key(self, i, key):
        if key < self.A[i][0]:
            raise ValueError('New key is smaller than current key.')
        self.A[i][0] = key
        while i > 1 and self.A[parent(i)][0] < self.A[i][0]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_mode):
        key, item = new_mode
        self.size += 1
        self.A.append([-np.inf, item])
        self.increase_key(self.size, key)


def main():
    max_pq = MaxBinaryHeapValue()

    print('Binary heap tuple with [5, a], [7, c], [3, b], [1, e]:')
    max_pq.insert([5, 'a'])
    max_pq.insert([7, 'c'])
    max_pq.insert([3, 'b'])
    max_pq.insert([1, 'd'])
    max_pq.show()

    print('Increase key 1 at position 4 to 6.')
    max_pq.increase_key(4, 6)
    max_pq.show()

    print('Find max:')
    print(max_pq.find_max())

    print('Extract max:')
    _max = max_pq.extract_max()
    print(_max)
    print('The remaining:')
    max_pq.show()

if __name__ == '__main__':
    main()
