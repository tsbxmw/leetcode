# 78. 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
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

# 先看 全排列吧

class Solution1:
    def subsets(self, nums):
        ln = len(nums)
        if ln == 0:
            return [[]]

        self.rev = []
        def dfs(nums, temp):
            if not nums:
                self.rev.append(temp)
                return
            for i, num in enumerate(nums):
                temp.append(num)
                dfs(nums[:i]+nums[i+1:], temp[:])
                temp.pop()
        dfs(nums, [])
        print(self.rev)
        return self.rev


# 全拍列改一改入库条件，这里其实不需要有排列，只是看数据
class Solution:
    def subsets(self, nums):
        ln = len(nums)
        if ln == 0:
            return [[]]

        def dfs(temp, nums, i):
            if i == ln:
                return temp
            v = [x[:] for x in temp]
            for t in temp:
                t.append(nums[i])

            temp = temp + v
            return dfs(temp, nums, i+1)

        return dfs([[]], nums, 0)
       
if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3,4,5]))