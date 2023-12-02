 '''
 LC 203 移除元素
 '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        
        Pointer = dummy_node
        while Pointer.next:
            if Pointer.next.val == val:
                Pointer.next = Pointer.next.next
            else:
                Pointer = Pointer.next
        return dummy_node.next
'''
LC 707设计链表
这题主要出现问题的是get
不知道为什么会越界
'''
class Node:
    def __init__(self, val = 0,next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.size = 0 
        self.dummny_node = Node()


    def get(self, index: int) -> int:
        if index < 0 or index > self.size:
            return -1
        '''
        pointer = dummny_node
        pos = -1
        '''
        '''
        pointer = self.dummny_node.next
        for _ in range (index):
            pointer = pointer.next
        '''
        '''
        while pos < index:
            pointer = pointer.next
            pos += 1
        '''
        
        
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummny_node.next
        for i in range(index):
            current = current.next
            
        return current.val

    def addAtHead(self, val: int) -> None:

        newhead = Node(val = val)
        newhead.next = self.dummny_node.next
        self.dummny_node.next = newhead
        self.size += 1


    def addAtTail(self, val: int) -> None:
        newTail = Node(val = val)
        '''
        pointer = head
        count = 0 

        while count != self.size-1:
            pointer = pointer.next
            count += 1 
        pointer.next = newTail
        '''
        cur = self.dummny_node
        while cur.next:
            cur = cur.next
        cur.next = newTail
        self.size += 1 


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        current = self.dummny_node
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.dummny_node
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


'''
LC 206, 主要的思考点在于对dummy_node的使用，
考虑什么是有需要从检测包括头节点位置
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(val = None, next = head)
        pre = None
        cur = dummy_node.next

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        return pre
