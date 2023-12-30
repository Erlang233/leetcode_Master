#530 二叉树最小绝对差
'''
首次用到了双指针
'''
class Solution_530:
    def __init__(self):
        self.result = float('inf')
        self.pre= None

        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.getMinimumDifference(root.left)
        if self.pre != None:
            self.result = min(self.result,root.val - self.pre)
        self.pre = root.val
        self.getMinimumDifference(root.right)
        return self.result

#501 二叉搜索树中的众数
class Solution_501:
    def __init__(self):
        self.dic = dict()
        self.result = []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.travel(root)
        count = max(self.dic.values())
        for key,value in self.dic.items():
            if value == count:
                self.result.append(key)
        
        return self.result
        

    def travel(self,root):
        if not root:
            return
        
        self.travel(root.left)
        if root.val not in self.dic:
            self.dic[root.val] = 1 
        else:
            self.dic[root.val] += 1
        self.travel(root.right)


# 236 二叉树的最近公共祖先

class Solution:
    def __init__(self):
        self.p1 = None
        self.p2 = None


        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        if root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right =self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        if not left and right:
            return right
        if not right and left:
            return left
        if not right and not left:
            return None
