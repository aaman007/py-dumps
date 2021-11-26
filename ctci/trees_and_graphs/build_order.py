"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies:
(a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c

from ctci.trees_and_graphs.build_order import SolutionX
s = SolutionX()
s.build_order(
    ['a', 'b', 'c', 'd', 'e', 'f'],
    [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]
)
"""

from collections import defaultdict, deque
from typing import List


class SolutionX:
    def build_order(self, projects, dependencies):
        adj = defaultdict(list)
        indegree = defaultdict(int)
        order = []
        queue = deque([])

        for projectA, projectB in dependencies:
            adj[projectA].append(projectB)
            indegree[projectB] += 1

        for project in projects:
            if not indegree[project]:
                queue.append(project)

        while queue:
            current_project = queue.popleft()
            order.append(current_project)

            for dependent in adj[current_project]:
                indegree[dependent] -= 1
                if not indegree[dependent]:
                    queue.append(dependent)

        if len(order) < len(projects):
            return None
        return order


""" Course Schedule LeetCode """


class Node:
    def __init__(self, value):
        self.value = value
        self.dependencies = 0
        self.children = []

    def getValue(self):
        return self.value

    def getNumberDependencies(self):
        return self.dependencies

    def getChildren(self):
        return self.children

    def addNeighbour(self, node):
        self.children.append(node)
        node.incrementDependencies()

    def incrementDependencies(self):
        self.dependencies += 1

    def decrementDependencies(self):
        self.dependencies -= 1


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = defaultdict(set)

    def createNode(self, value):
        self.nodes[value] = Node(value)

    def getOrCreateNode(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]

    def getNodes(self):
        return self.nodes.values()

    def addEdge(self, startValue, endValue):
        start = self.getOrCreateNode(startValue)
        end = self.getOrCreateNode(endValue)
        start.addNeighbour(end)


class Solution:
    def buildGraph(self, numCourses, prerequisites):
        graph = Graph()
        for course in range(numCourses):
            graph.createNode(course)

        for first, second in prerequisites:
            graph.addEdge(second, first)

        return graph

    def addNonDependent(self, courses, order):
        for course in courses:
            if not course.getNumberDependencies():
                order.append(course)

    def orderCourses(self, order):
        toBeProcessed = 0

        while toBeProcessed < len(order):
            currentCourse = order[toBeProcessed]
            toBeProcessed += 1

            for child in currentCourse.getChildren():
                child.decrementDependencies()

            self.addNonDependent(currentCourse.getChildren(), order)

        return order

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)

        order = []
        self.addNonDependent(graph.getNodes(), order)
        self.orderCourses(order)

        return len(order) == numCourses

