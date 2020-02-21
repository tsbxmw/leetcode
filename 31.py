# 31. 下一个排列
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


## key point:
### 1, 从后往前找递增序列
### 2，找到后，从后往前搜索比当前值小的值，到 递增序列的前面一个位置
### 例子
### 4202320     #从后往前找递增序列 320，
### 420 2320    #从后往前找比当前值小的值，搜索到递增序列之前的值 2320
### 420 232 0   #0 < 2, 0 < 3, 0 < 2, 0没有找到，向前遍历
### 420 23 2 0  #2 < 3, 2==2, 2没有找到，向前遍历
### 420 2 3 20  #3 > 2, 成立，交换 
###     | |
### 420 3 2 20  # 交换后，当前值和后面的值 220，进行排序
### 420 3 022   # 022
### 4203022
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
        temp = ln-1
        j = ln-1
        while j > 0:
            if nums[j-1]>=nums[j]:
                j -= 1
            else:
                break

        temp = j
        
        j = ln-1

        while j > temp-1:
            last = nums[j]
            for i in range(j-1, temp-2, -1):
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
    for i in range(20):
        s.nextPermutation(a)
        print(a)
    a=[1,2,3,4,5,6]
    for i in range(20):
        s.nextPermutation(a)
        print(a)
   