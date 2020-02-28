# 60. 第k个排列
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"


'''
## dfs
## 惯例 先来全排列
'''

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


# 全排列不直接算某个排列，而是不断地递归去寻找
# 这个非常类似 440 的方案，如果算出的数字大于当前的值，向下遍历。
class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"

        def get_count(nums):
            ln = len(nums)
            rev = 1
            for i in range(1, ln + 1):
                rev *= i
            return rev

        self.rev = ""
        nums = [i + 1 for i in range(n)]
        while k >= 0:
            i = 0
            while i < len(nums):
                count = get_count(nums[:i] + nums[i + 1:])  # 这里获取除了 以 nums[i] 剩下的数的全排列个数
                if count < k:   # 如果 count < k，说明我们需要的排列不在这个以 nums[i] 的向下序列里，所以， i+1 向后遍历 nums， 并把 k 更新为 k-count
                    i += 1
                    k -= count
                else:  # 如果 count <k 说明，我们需要的排列就在当前 nums[i] 所在的序列里， 将 nums[i] 放入结果中，更新 nums，既去除了当前 nums[i]的剩余序列
                    self.rev += str(nums[i])
                    nums = nums[:i] + nums[i + 1:]
                    break
            if len(nums) == 1:  # 这里要判断一下，如果只剩了最后一个数，直接 break，结果进入
                self.rev += str(nums[0])
                break
        return self.rev


if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(4, 9))

