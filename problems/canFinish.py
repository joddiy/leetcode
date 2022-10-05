from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph_ = defaultdict(list)
        for t1, t2 in prerequisites:
            graph_[t1].append(t2)

        visited = [0] * numCourses

        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1 or i not in graph_:
                return True

            visited[i] = -1
            for j in graph_[i]:
                if not dfs(j):
                    return False

            visited[i] = 1
            return True

        for i in list(graph_.keys()):
            if not dfs(i):
                return False

        return True


solution = Solution().canFinish

solution(2, [[1, 0]])
solution(2, [[1, 0], [0, 1]])
solution(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
