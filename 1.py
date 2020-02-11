# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 双层遍历

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        for i in range(ln):
            for j in range(i+1, ln):
                if nums[i] + nums[j] == target:
                    return [i, j]


## 先构建 map，查询需要的数是否存在

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        rmap = {nums[i]:i for i in range(ln)}

        for i in range(ln):
            r = target-nums[i]
            if r in rmap and i!=rmap[r]:
                return [i, rmap[r]]


## 创建 map 的同时检测是否有值

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        rmap = {}

        for i in range(0, ln):
            r = target-nums[i]
            if r in rmap and i!=rmap[r]:
                return [rmap[r], i]
            rmap[nums[i]] = i

