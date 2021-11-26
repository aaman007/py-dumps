"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""

from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        par = [p for p in range(n)]
        rank = [0 for _ in range(n)]

        def find(u: int) -> int:
            if par[u] == u:
                return u
            par[u] = find(par[u])
            return par[u]

        def merge(u: int, v: int):
            u, v = find(u), find(v)
            if u == v:
                return
            if rank[u] < rank[v]:
                u, v = v, u
            rank[u] += rank[v]
            par[v] = par[u]

        for u, v in edges:
            merge(u, v)

        return find(start) == find(end)


class SolutionWithDFS:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = [[] for _ in range(n)]
        vis = {}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def checkPath(source):
            if source == end:
                return True

            vis[source] = True
            for child in adj[source]:
                if not vis.get(child) and checkPath(child):
                    return True

            return False

        return checkPath(start)
