# 面试题 08.04. 幂集
# 幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

# 说明：解集不能包含重复的子集。

# 示例:

#  输入： nums = [1,2,3]
#  输出：
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.rev = None

        def dfs(nums, temp):
            if not nums:
                self.rev = temp
                return
            d = [x[:] for x in temp]
            for x in temp:
                x.append(nums[0])
            dfs(nums[1:], d+temp)

        dfs(nums, [[]])

        return self.rev