from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_binary_heap_tuple import BinaryHeap

def dijkstra(graph, vertex_start):
    pass

def main():
    weight_graph = {
        'u': {'v': 2, 'w': 5, 'x': 1},
        'v': {'u': 2, 'w': 3, 'x': 2},
        'w': {'u': 5, 'v': 3, 'x': 3, 'y': 1, 'z': 5},
        'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1},
        'y': {'w': 1, 'x': 1, 'z': 1},
        'z': {'w': 5, 'y': 1}
    }
    print(weight_graph)

    bh = BinaryHeap()

if __name__ == '__main__':
    main()
