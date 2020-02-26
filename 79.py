# 79. 单词搜索
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.

## 深度搜索

class Solution:
    def exist(self, board, word: str) -> bool:
        if not word:
            return True
        li = len(board)
        if li == 0:
            return False
        lj = len(board[0])
        if lj == 0:
            return False
        lw = len(word)
        def dfs(i, j, li, lj, x, lw, board):
            if x == lw:
                return True
            if 0<=i<li and 0<=j<lj:
                print(i, j, x, word[x], board[i][j], board)
                if board[i][j] and board[i][j] == word[x]:
                    board[i][j] = ''
                    return dfs(i+1, j, li, lj, x+1, lw, [y[:] for y in board]
                               ) or dfs(i-1, j, li, lj, x+1, lw, [y[:] for y in board]
                                        ) or dfs(i, j-1, li, lj, x+1, lw, [y[:] for y in board]
                                                 ) or dfs(i, j+1, li, lj, x+1, lw, [y[:] for y in board])
                else:
                    return False
            else:
                return False

        i, j = 0, 0

        while i < li:
            j = 0
            while j < lj:
                temp = [y[:] for y in board]
                if dfs(i, j, li, lj, 0, lw, temp):
                    return True
                j += 1
            i += 1
        return False


if __name__ == "__main__":
    s = Solution()
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED"
    word1 = "SEE"
    word2 = "ABCB"

    print(s.exist(board, word))
    print(s.exist(board, word1))
    print(s.exist(board, word2))
