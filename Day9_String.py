"""
以此排序是 LC 28 
自己做的时候使用滑动窗口来做的
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        interval = len(needle)
        left, right = 0, interval - 1
        while right < len(haystack) :
            if (haystack[left]== needle[0] and haystack[right] == needle[-1]):
                test = True
                for i in range (left,right + 1):
                    if haystack[i] != needle[i-left]:
                        test = False
                        break
                    
                if test:
                    return left

            left += 1
            right +=1
        return -1

#KMP
class Solution:
    def getNext(self,next,s):
        j = -1
        next[0] = j 
        for i in range (1,len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j+= 1
            next[i] = j
    
    '''
    A = 'aabaabaaf' b = 'aabaaf'
    对于b取getnext 
    next = [-1,0,-1 ,1,2,0]
    i = 1: j = -1 + 1 = 0
    i = 2: j= 0,s[i] =b != s[j+1] = a, j = next[j] = -1
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0 
        n =len(needle)
        next = [0] * n 
        self.getNext(next,needle)
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]:
                j = next[j]
            if haystack[i] == needle[j+1]:
                j+= 1
            if j == n-1:
                return i-n+1
        
        return -1
