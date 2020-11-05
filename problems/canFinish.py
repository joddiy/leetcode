def solution(numCourses, prerequisites):
    grid = [[] for _ in range(numCourses)]
    visited = [0] * numCourses

    for i, j in prerequisites:
        grid[i].append(j)

    def recusive(i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True

        visited[i] = -1
        for j in grid[i]:
            if not recusive(j):
                return False

        visited[i] = 1
        return True

    for i in range(numCourses):
        if not recusive(i):
            return False
    return True


# print(solution(2, [[1, 0]]))
print(solution(2, [[1, 0], [0, 1]]))
