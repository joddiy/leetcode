from tools import *


class Solution(object):
    # BFS
    @print_
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        m, n = len(board), len(board[0])
        queue = []
        # add the 'O' at border into the queue
        for i in range(n):
            if board[0][i] == "O":
                queue.append((0, i))
            if board[m - 1][i] == "O":
                queue.append((m - 1, i))

        for i in range(1, m - 1):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][n - 1] == "O":
                queue.append((i, n - 1))

        # BFS
        while queue:
            i, j = queue.pop(0)
            board[i][j] = '.'

            if i - 1 >= 0 and board[i - 1][j] == 'O':
                queue.append((i - 1, j))
            if i + 1 < m and board[i + 1][j] == 'O':
                queue.append((i + 1, j))
            if j - 1 >= 0 and board[i][j - 1] == 'O':
                queue.append((i, j - 1))
            if j + 1 < n and board[i][j + 1] == 'O':
                queue.append((i, j + 1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                elif board[i][j] == ".":
                    board[i][j] = 'O'
        return board


solution = Solution().solve

solution([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"],
          ["X", "O", "X", "X"]])
