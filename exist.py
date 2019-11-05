class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(
            board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

    #
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nrow = len(board)
        ncol = len(board[0])
        nword = len(word)

        def dfs(row, col, idx):
            if idx == nword:
                return True
            board[row][col] = '#'
            if row+1 < nrow and board[row+1][col] == word[idx] and dfs(row+1, col, idx+1):
                return True
            if row-1 >= 0 and board[row-1][col] == word[idx] and dfs(row-1, col, idx+1):
                return True
            if col+1 < ncol and board[row][col+1] == word[idx] and dfs(row, col+1, idx+1):
                return True
            if col-1 >= 0 and board[row][col-1] == word[idx] and dfs(row, col-1, idx+1):
                return True
            board[row][col] = word[idx-1]
            return False
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False


print(Solution().exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'ABCCED'))
