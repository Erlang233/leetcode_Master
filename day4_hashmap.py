#LC 454 
'''
code总提来说不难
双指针更容易理解
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        minusNumbers = {}
        n = len(nums1)
        count = 0
        for i in range (n):
            for j in range (n):
                if nums1[i] + nums2[j] not in minusNumbers:
                    minusNumbers[nums1[i]+nums2[j]] = 1 
                else: 
                    minusNumbers[nums1[i]+nums2[j]] += 1 

        for i in range(n):
            for j in range(n):
                remain = 0 - nums3[i]-nums4[j]
                if remain in minusNumbers:
                    count += minusNumbers[remain]
        
        return count


#LC 383  有一个巧思，在于第二个for loop选择key上面

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        r_dict = defaultdict(int)
        m_dict = defaultdict(int)

        for i in ransomNote:
            r_dict[i] += 1 

        for j in magazine:
            m_dict[j] += 1

        for key in r_dict:
            if m_dict[key] < r_dict[key]:
                return False

        return True 
# 15 三数之和
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range (n):
            a = nums[i]
            if a > 0:
                return result
            
            if i > 0 and a == nums[i - 1]:
                continue
            left = i+1
            right = n - 1
            while left < right: 
                total = nums[left] + nums[right] + a 
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1 
                else:
                    result.append([a,nums[left],nums[right]])
                    while nums[right] == nums[right - 1] and right > left:
                        right -= 1
                    while nums[left] == nums[left + 1] and  left < right:
                        left += 1 
                    right -= 1 
                    left += 1 
        
        return result


#四数之和 需要去重的版本
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:# 剪枝（可省）
                break
            if i > 0 and nums[i] == nums[i-1]:# 去重
                continue
            for j in range(i+1, n):
                if nums[i] + nums[j] > target and target > 0: #剪枝（可省）
                    break
                if j > i+1 and nums[j] == nums[j-1]: # 去重
                    continue
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result
