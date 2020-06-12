def solution(board, word):
    m, n = len(board), len(board[0])

    def recursion(i, j, idx):
        if idx == len(word):
            return True
        board[i][j] = "#"
        if i + 1 < m and board[i + 1][j] == word[idx] and recursion(
                i + 1, j, idx + 1):
            return True
        if j + 1 < n and board[i][j + 1] == word[idx] and recursion(
                i, j + 1, idx + 1):
            return True
        if i - 1 >= 0 and board[i - 1][j] == word[idx] and recursion(
                i - 1, j, idx + 1):
            return True
        if j - 1 >= 0 and board[i][j - 1] == word[idx] and recursion(
                i, j - 1, idx + 1):
            return True
        board[i][j] = word[idx - 1]
        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and recursion(i, j, 1):
                return True
    return False


print(
    solution([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
             "ABCCED"))
