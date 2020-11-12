from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])

        def recursive(i, j, idx, word):
            s = len(word)
            if idx == s:
                return True
            board[i][j] = "#"
            if i - 1 >= 0 and board[i - 1][j] == word[idx] and recursive(
                    i - 1, j, idx + 1, word):
                board[i][j] = word[idx - 1]
                return True
            if j - 1 >= 0 and board[i][j - 1] == word[idx] and recursive(
                    i, j - 1, idx + 1, word):
                board[i][j] = word[idx - 1]
                return True
            if i + 1 <= m - 1 and board[i + 1][j] == word[idx] and recursive(
                    i + 1, j, idx + 1, word):
                board[i][j] = word[idx - 1]
                return True
            if j + 1 <= n - 1 and board[i][j + 1] == word[idx] and recursive(
                    i, j + 1, idx + 1, word):
                board[i][j] = word[idx - 1]
                return True
            board[i][j] = word[idx - 1]

        ret = set()
        for word in words:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0] and recursive(i, j, 1, word):
                        ret.add(word)
        return list(ret)


solution = Solution().findWords

# solution(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"],
#                 ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
#          words=["oath", "pea", "eat", "rain"])

# solution(board=[["a", "b"], ["c", "d"]], words=["abcb"])
# solution(board=[["a", "a"]], words=["a"])
solution(board=[["a", "b"], ["c", "d"]],
         words=[
             "ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb",
             "dabc", "abb", "acb"
         ])
