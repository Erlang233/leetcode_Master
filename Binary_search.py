# 11.28.2023 代码随想录
# from leetcode 704,35,26. 34还不会
'''
searching the target form mid[left,right], right place should also be included
everytime the program enter into a new iteration, left should be replaced to mid + 1 and right should be repalced by 
mid -1 due to the mid place is aleady checked
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
         
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right -left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1


'''
searching the target form mid[left,right), right place should also be included
everytime the program enter into a new iteration, left should be replaced to mid + 1 and right should be repalced by 
mid due to the mid place is aleady checked
'''
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left +(right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
            
        return -1 
    
# leetcode 35
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)

        while left < right:
            mid = left + (right-left) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left


#代码随想录这个看起来更简单
def removeElement(self, nums: List[int], val: int) -> int:

    slow,fast = 0, 0
    size = len(nums)

    while fast < size:
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    
    return slow 
# 26. remove duplicate
def removeDuplicates(self, nums: List[int]) -> int:
    left, right = 0, 0
    size = len(nums)
    #323456
    while right < size:

        if nums[right] != nums[left]:
            nums[left+1] = nums[right]
            left += 1
        right += 1
    
    return left + 1
