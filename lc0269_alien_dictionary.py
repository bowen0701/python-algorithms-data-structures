"""Leetcode 269. Alien Dictionary (Premium)
Hard

URL: https://leetcode.com/problems/alien-dictionary

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from
the dictionary, where words are sorted lexicographically by the rules of this
new language. Derive the order of letters in this language.

Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"

Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
] 
Output: "" 
Explanation: The order is invalid, so return "".

Note:
- You may assume all letters are in lowercase.
- You may assume that if a is a prefix of b, then a must appear before b in the 
  given dictionary.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.
"""

class SolutionTopologicalSort(object):
    def _build_graph(self, words):
        from collections import defaultdict

        graph = defaultdict(set)
        indegrees = defaultdict(int)

        # Create graph:each char -> set.
        for w in words:
            for c in w:
                graph[c] = set()

        # Build graph and indegrees in order of words with different chars.
        for i in range(1, len(words)):
            w_from = words[i - 1]
            w_to = words[i]

            min_len = min(len(w_from), len(w_to))

            for j in range(min_len):
                c_from = w_from[j]
                c_to = w_to[j]

                if c_from != c_to:
                    if c_to not in graph[c_from]:
                        graph[c_from].add(c_to)
                        indegrees[c_to] += 1

                    # Break after get the 1st different char.
                    break

        return graph, indegrees

    def _topological_sort(self, graph, indegrees):
        # Build ordered string based on indegrees by Kahn's algorithm.
        from collections import deque

        # Put char into zero indegree queue if its indegree is 0.
        queue = deque([])
        for c in graph:
            if indegrees[c] == 0:
                queue.appendleft(c)

        order_chars = []

        while queue:
            # Remove zero in-degree char c and add it to order chars.
            c = queue.pop()
            order_chars.append(c)

            # Visit zero indegree char's neighbors and decrement indegrees.
            for c_next in graph[c]:
                indegrees[c_next] -= 1

                # If c's neighbor has zero in-degrees, append to queue.
                if indegrees[c_next] == 0:
                    queue.appendleft(c_next)

        return order_chars

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str

        Apply Kahn's algorithm for topological sort for string order.

        Time complexity: O(n*m), where 
          - n: length of words
          - m: max number of chars in words
        Space complexity: O(1), since we have fixed number of chars.
        """
        # Edge case.
        if not words or not words[0]:
            return ''

        # Build dict graph:char_from->set(char_to) and dict indegrees:to_char->count.
        graph, indegrees = self._build_graph(words)

        # Apply Topological Sort to create string order.
        order_chars = self._topological_sort(graph, indegrees)

        # Check if length of string order is the same as that of graph keys.
        if len(order_chars) == len(graph.keys()):
            return ''.join(order_chars)
        else:
            return ''


def main():
    # Output: "wertf"
    words = [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]
    print SolutionTopologicalSort().alienOrder(words)

    # Output: "zx"
    words = [
      "z",
      "x"
    ]
    print SolutionTopologicalSort().alienOrder(words)

    # Output: ""
    words = [
      "z",
      "x",
      "z"
    ] 
    print SolutionTopologicalSort().alienOrder(words)

    # Output: "wertf"
    words = [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt",
      "te"
    ]
    print SolutionTopologicalSort().alienOrder(words)


if __name__ == '__main__':
    main()
