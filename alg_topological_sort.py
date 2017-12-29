from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsited_d, clock):
    clock += 1
    previsited_d[v] = clock
    return previsited_d, clock

def _postvisit(v, postvisited_d, clock):
    clock += 1
    postvisited_d[v] = clock
    return postvisited_d, clock

def _dfs_explore(v, dag_adj_d, visited_d,
                 previsited_d, postvisited_d, clock):
    visited_d[v] = True
    previsited_d, clock = _previsit(v, previsited_d, clock)
    for v_neighbor in dag_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsited_d, postvisited_d, clock = (
                _dfs_explore(v_neighbor, dag_adj_d, visited_d,
                             previsited_d, postvisited_d, clock))
    postvisited_d, clock = _postvisit(v, postvisited_d, clock)
    return visited_d, previsited_d, postvisited_d, clock

def topological_sort(dag_adj_d):
    """Topological Sorting for Directed Acyclic Graph (DAG).

    To topologically sort a DAG, we simply do depth first search,
    then arrange DAG's vertices in decreasing order of postvisits.
    """
    visited_d = {v: False for v in dag_adj_d.keys()}
    previsited_d = {}
    postvisited_d = {}
    clock = 0
    for v in dag_adj_d.keys():
        if not visited_d[v]:
            visited_d, previsited_d, postvisited_d, clock = (
                _dfs_explore(v, dag_adj_d, visited_d,
                             previsited_d, postvisited_d, clock))
    rev_postvisited_d = {postvisited_d[k]: k for k in postvisited_d.keys()}
    topological_sort_ls = []
    for v in reversed(sorted(rev_postvisited_d.keys())):
        topological_sort_ls.append(rev_postvisited_d[v])
    return topological_sort_ls


def main():
    # DAG.
    dag_adj_d = {
        'A': ['B', 'F'],
        'B': ['C', 'D', 'F'],
        'C': ['D'],
        'D': ['E', 'F'],
        'E': ['F'],
        'F': []
    }

    topological_sort_ls = topological_sort(dag_adj_d)
    print(topological_sort_ls)

if __name__ == '__main__':
    main()
