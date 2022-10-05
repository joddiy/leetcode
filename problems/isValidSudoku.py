from tools import *


@print_
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    boxes = [None] * 9
    rows = [None] * 9
    columns = [None] * 9
    for i in range(9):
        for j in range(9):
            t = board[i][j]
            if t != ".":
                if rows[i] is None:
                    rows[i] = set()
                if t in rows[i]:
                    return False
                else:
                    rows[i].add(t)

                if columns[j] is None:
                    columns[j] = set()
                if t in columns[j]:
                    return False
                else:
                    columns[j].add(t)

                k = j // 3 * 3 + i // 3
                if boxes[k] is None:
                    boxes[k] = set()
                if t in boxes[k]:
                    return False
                else:
                    boxes[k].add(t)
    return True


isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
