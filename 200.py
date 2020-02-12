# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ll = len(grid)
        if ll == 0:
            return 0
        lr = len(grid[0])
        if lr == 0:
            return 0
        self.ans = 0

        def search(i, j, flag):
            if i < 0 or i >= ll:
                return
            if j < 0 or j >= lr:
                return

            if grid[i][j] == '0':
                return
            elif flag:
                self.ans += 1
                flag = False
            grid[i][j] = '0'
            search(i-1, j, flag)
            search(i+1, j, flag)
            search(i, j-1, flag)
            search(i, j+1, flag)
        for i in range(ll):
            for j in range(lr):
                if grid[i][j] == "1":
                    search(i, j, True)

        return self.ans
    