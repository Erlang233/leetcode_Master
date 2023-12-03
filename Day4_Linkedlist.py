#LC 142 环形列表
'''
在本题中，几个需要想通的地方
1. 如何证明有环，这个时候就可以用到双指针，两个指针在环中如有重叠的问题，就可证明有环
2. 因为是同向出发，只能使用快慢指针，那怎么确定快指针和慢指针不会有永不重叠的现象呢？
答案是将快指针的速度设为二，将慢指针的速度设为1，这样，当快慢指针同时进入环中（如有），
快指针将会以每次iteration加快一个步长的速度追赶慢指针，以确保不会错过。
3.假设有环，且快慢指针相遇，如何寻找环的入口呢？
设三段距离，首个节点到环入口为x，入口到现在快慢指针的位置为y，快慢指针距离下一次到
入口的距离为z。
假设当快指针进入环中n圈后与慢指针相遇。
x+y(一会来解释这里) = （x+y +n(z+y)）/2 （抵达相同位置）可以理解为时间。
x = n(z+y) - y
x = (n-1)(z+y) + z
因为这里的n >= 1，（n代表圈数）。则多项式的前半段都处于完成环型步长的总次数，与x
长度不相关，约成0， x = z。
为什么x不会走多个环型呢？
假设在慢指针初次抵达环入口时，快指针在任意位置，且距离环口距离为k（k小于总环长n）
则快指针到下次环口的时间是（k+n）/2，这也同样是慢指针能走过的距离。
在此段行程中，因为快指针在慢指针进入环后又完成了一圈，所以他们必定在图中就相遇了。
因此，慢指针无法走过多个圈。
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head, head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            if fast == slow:
                new = head
                new1 = fast
                while new != new1:
                    new = new.next
                    new1 = new1.next
                return new
        
        return None

# LC面试题 02.07. 链表相交 没啥说的，理解完题目就会了

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:         # 求链表A的长度
            cur = cur.next 
            lenA += 1
        cur = headB 
        while cur:         # 求链表B的长度
            cur = cur.next 
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA 
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next 
        while curA:         #  遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next 
                curB = curB.next
        return None         


#LC 19，移除倒数第n个数
'''
可以直接设一个哨兵节点，将快慢指针的距离变为n+1（我通过dummyNode来实现的+1），确保当fast到最后时
慢指针到达了需要移除的上一个节点，方可直接移除。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode = ListNode(next = head)
        slow, fast = dummynode,dummynode
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummynode.next 

'''
LC 24,注意可以用哨兵节点，方便直接操作第一个节点
每两个节点开始修改位置，注意每次修改完之后，现节点直接指向next.next 而不是next。
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 
        dummyNode = ListNode(next = head)
        cur = dummyNode
        while cur.next and cur.next.next:
            temp = cur.next.next.next
            temp1 = cur.next
            cur.next = cur.next.next
            cur.next.next = temp1
            temp1.next = temp
            cur = temp1

            
        
        return dummyNode.next 
            


