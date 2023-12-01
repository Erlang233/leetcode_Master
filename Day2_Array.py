#LC 977
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newlist = [None] * n
        left, right, new = 0, n -1, n -1
        while left <= right: 
            if nums[left] ** 2 > nums[right] ** 2:
                newlist[new] = nums[left]**2
                left += 1
            else:
                newlist[new] = nums[right]**2
                right -=1 
            new -= 1 
        
        return newlist
#LC 977

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newlist = []
        for i in nums:
            newlist.append(i**2)
        newlist.sort()
        return newlist

# LC 209

class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast = 0, 0
        result = len(nums) + 1
        count= nums[fast]
        while fast < len(nums):
            if count >= target:
                result = min(result,fast-slow+1)
                count-= nums[slow]
                slow += 1
            else:
                fast+=1
                if fast == len(nums):
                    break 
                count+= nums[fast]
        return result if result < len(nums) +1 else 0


#LC 59

class Solution3:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)]for _ in range(n)]

        starty, startx = 0 , 0
        offset = 1
        count = 1
        route = 1
        while(route <= n // 2):
            i, j = startx, starty
            while(j < n - offset):
                matrix[i][j] = count
                j += 1
                count += 1
            print(matrix)
            while(i < n -offset):
                matrix[i][j] = count
                i += 1
                count += 1
            print(matrix)
            while(j > offset -1 ):
                matrix[i][j] = count
                j -= 1
                count += 1
            print(matrix)
            while(i > offset -1):
                matrix[i][j] = count
                i -= 1
                count += 1
            print(matrix)
            route += 1
            startx += 1
            starty += 1
            offset += 1 
            
        if(n % 2 == 1):
            matrix[startx][starty] = count
        
        return matrix
            
