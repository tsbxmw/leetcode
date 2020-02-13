# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

#  



# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

#  



# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

#  

# 示例:

# 输入: [2,1,5,6,2,3]
# 输出: 10

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 暴力求解优化

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxall = 0
        ln = len(heights)
        for i in range(ln):
            l = 1
            minh = heights[i]
            for j in range(i, ln):
                minh = min(minh, heights[j])
                maxall = max(maxall, l*minh)
                if heights[j] == 0 or j == ln-1:
                    break
                
                l += 1
        return maxall



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]
        maxall = 0
        lh = len(heights)
        for i in range(lh):
            if i == 0:
                stack.append((i, heights[i]))
            else:
                if heights[i] >= stack[-1][1]:
                    stack.append((i, heights[i]))
                else:
                    while len(stack) > 1 and stack[-1][1] >= heights[i]:
                        maxall = max(maxall, (i-1-stack[-2][0])*stack[-1][1])
                        stack.pop()

                    stack.append((i, heights[i]))
        
        while len(stack) > 1:
            maxall = max(maxall, (lh-1-stack[-2][0])*stack[-1][1])
            stack.pop()
        return maxall

## 单调栈

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]

        maxall = 0
        heights.append(0)
        lh = len(heights)

        for i in range(lh):
            if i == 0:
                stack.append((heights[i], i))
            else:
                if heights[i] >= stack[-1][0]:
                    stack.append((heights[i], i))
                else:
                    while len(stack) > 1 and stack[-1][0] >= heights[i]:
                        maxall = max(maxall, stack[-1][0] * (i-stack[-2][1]-1)) # 这里 右边界就是 i，即比 上面的循环中 比顶部元素 小的右边的 边界， 左边界 即 顶部第二个元素的值得右边。 即 i(右边) - （stack[-2][1]+1） (左边元素+ 1） 是底，高的话就是当前顶部元素的值了
                        stack.pop() # 栈顶元素出栈
                    stack.append((heights[i], i)) # 找到了比当前元素小的位置，直接插入，如果栈空了，也一样
        return maxall