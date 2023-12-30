#  修建二叉搜说树
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None
        if root.val < low:
            # 寻找符合区间 [low, high] 的节点
            return self.trimBST(root.right, low, high)
        if root.val > high:
            # 寻找符合区间 [low, high] 的节点
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)  # root.left 接入符合条件的左孩子
        root.right = self.trimBST(root.right, low, high)  # root.right 接入符合条件的右孩子
        return root



# 108 有序数组中创建二叉树 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.construct(nums)

    def construct(self,nums):
        n = len(nums)
        if not nums:
            return
        if n//2 == 0:
            return TreeNode(nums[0])
        
        cur = TreeNode(nums[n//2])
        cur.left = self.construct(nums[:(n//2)])
        cur.right = self.construct(nums[(n//2)+1:])
        
        return cur



#538 二叉树换成累加树

class Solution:
    def __init__(self):
        self.count = 0 
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.travel(root)
        return root
    def travel(self,root):
        if not root:
            return 
        self.travel(root.right)
        self.count += root.val
        root.val = self.count
        self.travel(root.left)
