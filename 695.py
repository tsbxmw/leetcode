# 695. 岛屿的最大面积
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

# 示例 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

# 示例 2:

# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。

# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        leni = len(grid)
        if leni == 0:
            return 0

        lenj = len(grid[0])
        if lenj == 0:
            return 0

        self.rev = 0

        def dfs(grid, i, j, temp):
            if i < 0 or i >= leni or j < 0 or j >= lenj:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            temp = temp+1
            one = dfs(grid, i+1, j, 0)
            two = dfs(grid, i-1, j, 0)
            three = dfs(grid, i, j-1, 0)
            four = dfs(grid, i, j+1, 0)
            temp = one+two+three+four+temp

            self.rev = max(self.rev, temp)

            return temp

        for i in range(leni):
            for j in range(lenj):
                if grid[i][j] == 1:
                    dfs(grid, i, j, 0)

        return self.rev
