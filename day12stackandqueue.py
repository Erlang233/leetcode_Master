from collections import deque

class myque():
    def __init__(self):
        self.que = deque()

    def pop(self, e):
        if self.que and self.que[0] == e:
            self.que.popleft()

    def push(self,e):
        while self.que and e > self.que[-1]:
            self.que.pop()
        self.que.append(e)

    def getMax(self):
        return self.que[0]
        
    




class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [] 
        que = myque()
        for i in range(k):
            que.push(nums[i])
        result.append(que.getMax())

        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.getMax())
        
        return result


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
