# 54. 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


# 按照 left -> down -> right -> up 即可
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        li = len(matrix)
        if li == 0:
            return []
        if li == 1:
            return matrix[0]

        lj = len(matrix[0])
        self.rev = []
        count = li * lj

        def test(i, j, li, lj):
            if count == len(self.rev):
                return self.rev
            # right:
            while j < lj and isinstance(matrix[i][j], int):
                self.rev.append(matrix[i][j])
                matrix[i][j] = ''
                j += 1
            j -= 1
            i += 1
            # down:
            while i < li and isinstance(matrix[i][j], int):
                self.rev.append(matrix[i][j])
                matrix[i][j] = ''
                i += 1
            i -= 1
            j -= 1
            # left:
            while j >= 0 and isinstance(matrix[i][j], int):
                self.rev.append(matrix[i][j])
                matrix[i][j] = ''
                j -= 1
            j += 1
            i -= 1
            # up
            while i >= 0 and isinstance(matrix[i][j], int):
                self.rev.append(matrix[i][j])
                matrix[i][j] = ''
                i -= 1
            i += 1
            j += 1
            return test(i, j, li, lj)

        return test(0, 0, li, lj)
