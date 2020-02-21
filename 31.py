# 31. 下一个排列
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        if ln == 0:
            return
        flag = False
        flag_temp = False
        j = ln-1
        while j > 0:
            if nums[j-1]>=nums[j]:
                j -= 1
            else:break
            
        if j == 1:
            j = ln-1

        while j > 0:
            last = nums[j]
            for i in range(j-1, -1, -1):
                if nums[i] < last:
                    nums[j] = nums[i]
                    nums[i] = last
                    a = nums[i+1:]
                    a.sort()
                    nums[i+1:] = a
                    flag = True
                    break
            if flag:
                break
            else:
                j-=1

        if not flag:
            nums.sort()


if __name__ == "__main__":
    s = Solution()
    a=[4,2,0,2,3,2,0]
    for i in range(50):
        s.nextPermutation(a)
        print(a)
    a=[1,2,3,4,5,6]
    for i in range(50):
        s.nextPermutation(a)
        print(a)
   