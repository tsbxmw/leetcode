# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#  

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 双指针遍历，最主要去除重复的元素的干扰

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        if ln <= 2:
            return []
        if ln == 3 and sum(nums) == 0:
            return [nums]
        nums.sort()
        if nums[0] > 0:
            return []
        temp = []
        x = 1
        while x < ln:
            if nums[x-1] > 0:
                break
            j = ln - 1
            i = x
            while i < j:
                sum_xij = nums[x-1] + nums[i] + nums[j]
                if sum_xij == 0:
                    temp.append([nums[x-1], nums[i], nums[j]])
                    i += 1
                    j -= 1                    
                    while j<ln-1 and j>=0 and nums[j] == nums[j+1]:
                        j -= 1
                    while i>0 and i<=ln-1 and nums[i] == nums[i-1]:
                        i += 1
                elif sum_xij > 0:
                    j -= 1
                    while j<ln-1 and j>=0 and nums[j] == nums[j+1]:
                        j -= 1
                        if i>=j:
                            break
                else:
                    i += 1
                    while i>0 and i<=ln-1 and nums[i] == nums[i-1]:
                        i += 1
                        if i>=j:
                            break
            
            while x < ln and nums[x] == nums[x-1]:
                x+=1
            x+=1
        return temp