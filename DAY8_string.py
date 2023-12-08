#LC 344 反转字符串
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 原地反转,无返回值
        s.reverse()

#LC541反转字符串II
'''
这题不用分类讨论，题意不是很好理解，不是说的每2k个数就反转前半部分，总的来说，题目略脑残
只有两个情况：
1.总数小于k时，反转所有
2.如果大于k，反转前面
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      n = len(s)
      start = 0
      org = list(s)

      for i in range(0,n,2*k):
        temp = org[i:i+k]
        temp = temp[::-1]
        org[i:i+k] = temp

      return ''.join(org)
# LC151 反转字符串当中的单词

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        n = len(s)
        slow, fast = 0, 0 
        while fast < n:
            if s[fast] == "":
                fast += 1
            else:
                s[slow] = s[fast]
                slow += 1 
                fast += 1
        
        s= s[:slow][::-1]
        return " ".join(s)
