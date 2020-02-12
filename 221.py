# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 示例:

# 输入: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-square
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        dp = [[int(y) for y in x] for x in matrix]

        lm = len(matrix)
        if lm == 0:
            return 0
        ln = len(matrix[0])
        if ln == 0:
            return 0

        def search(i, j):
            if i <= 0 or i > lm-1:
                return
            if j <= 0 or j > ln-1:
                return
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        for i in range(lm):
            for j in range(ln):
                if matrix[i][j] == '1':
                    search(i, j)
        return max([max(x) for x in dp]) ** 2

                    
