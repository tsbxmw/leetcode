# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/daily-temperatures
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 暴力求解，rot
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp = []
        lt = len(T)
        for i in range(lt):
            if i>=1:
                if T[i] == T[i-1]:
                    temp.append(temp[-1]-1 if temp[-1] > 0 else 0)
                    continue
            flag = False
            for j in range(i+1, lt):
                if T[i] < T[j]:
                    temp.append(j-i)
                    flag = True
                    break
            if not flag:
                temp.append(0)
        
        return temp
            
## 用 stack

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        lt = len(T)
        temp = [(T[-1], lt-1)]

        rev = [0]
        i = lt-2
        while i >= 0:
            ltemp = len(temp)
            flag = False
            for j in range(ltemp-1, -1, -1):
                if temp[j][0] > T[i]:
                    rev.append(temp[j][1] - i)
                    flag = True
                    break
                else:
                    temp.pop()
            if not flag:
                rev.append(0)
                
            temp.append((T[i], i))
            i -= 1

        return rev[::-1]
        

