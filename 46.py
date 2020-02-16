# 给定一个没有重复数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 这个是典型的回溯算法

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        lt = len(nums)

        if lt == 0:
            return []
        if lt == 1:
            return [nums]

        def test(nums, temp, current, lt):

            if len(current) == lt:
                temp.append(current)

            if not nums:
                return

            for i, x in enumerate(nums):
                current.append(x) ## 这里先 append，使用完后 再 pop
                test(nums[:i] + nums[i+1:], temp, current[::], lt)  ## 这里要记得是除了当前元素被使用了，剩下的 [:i]+[i+1:] 都要到下层的遍历
                current.pop()
            return temp
        temp = test(nums, [], [], lt)
        return temp

