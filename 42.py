# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def trap(self, height: List[int]) -> int:
        ln = len(height)

        if ln == 0 or ln == 1 or ln == 2:
            return 0

        i = 0
        j = ln - 1
        left = height[i]
        right = height[j]
        maxh = 0
        rev = 0

        while i < j:
            if height[i] == height[j]:
                left = height[i]
                i += 1
                continue

            if height[i] < height[j]:
                if left > height[i]:
                    rev += left - height[i]
                else:
                    left = height[i]
                i += 1
            else:
                if right > height[j]:
                    rev += right - height[j]
                else:
                    right = height[j]
                j -= 1
        return rev

            


