#有效的字母异位词

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count


#有效的字母异位词2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Dic = [0]*26
        
        for i in s:
            pos = ord(i)-ord('a')
            Dic[pos] += 1

        for j in t:
            pos = ord(j)-ord('a')
            Dic[pos] -= 1


        for i in Dic:
            if i != 0:
                return False 

        return True   

#两个数组的交集
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = list(nums1.intersection(nums2))

        return result 


#快乐数
class Solution:
    def isHappy(self, n: int) -> bool:
        sumset = set()
        def newsum(num):
            newNum = 0 
            while num:
                num, r = divmod(num, 10)
                newNum += r ** 2

            return newNum
        while True:
            newN = newsum(n)
            print(newN)
            if newN == 1:
                return True

            else:
                if newN in sumset:
                    return False
                else:
                    sumset.add(newN)
                    n = newN


#两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hT = dict()
        for i, num in enumerate(nums):
            if target - num in hT:
                return [hT[target - num], i]
            hT[nums[i]] = i
        
        return False
        
