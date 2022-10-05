from tools import *


class Solution(object):
    @print_
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        l = len(word)

        def find(i, j, idx):
            if idx == l:
                return True
            else:
                board[i][j] = '#'
                if i - 1 >= 0 and board[i - 1][j] == word[idx] and find(
                        i - 1, j, idx + 1):
                    return True
                if i + 1 < m and board[i + 1][j] == word[idx] and find(
                        i + 1, j, idx + 1):
                    return True
                if j - 1 >= 0 and board[i][j - 1] == word[idx] and find(
                        i, j - 1, idx + 1):
                    return True
                if j + 1 < n and board[i][j + 1] == word[idx] and find(
                        i, j + 1, idx + 1):
                    return True
                board[i][j] = word[idx - 1]
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 1):
                    return True
        return False


solution = Solution().exist

solution([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
         "ABCCED")
