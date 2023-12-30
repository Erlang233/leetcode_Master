# 654最大二叉树
# 思考和之前的构造二叉树类似
class Solution_654:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        
        maxi = max(nums)
        root = TreeNode(maxi)
        
        breakP = nums.index(maxi)
        root_left = nums[:breakP]
        root_right = nums[breakP+1:]
        
        root.left = self.constructMaximumBinaryTree(root_left)
        root.right = self.constructMaximumBinaryTree(root_right)

        return root


# 617 合并二叉树
class Solution_617:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        if not root1 and root2:
            return root2
        if root1 and not root2:
            return root1
        
        New_root = TreeNode(root1.val + root2.val)
        New_root.left = self.mergeTrees(root1.left, root2.left)
        New_root.right =self. mergeTrees(root1.right,root2.right)
        return New_root


#700 二叉搜索树中的搜说
class Solution_700:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        if not root:
            return 
        if root.left and val < root.val:
            left = self.searchBST(root.left, val)
            return left
        if root.right and val > root.val:
            right = self.searchBST(root.right,val)
            return right



#98 验证二叉树
'''
主要的关键不是检查但也节点和根节点的match，而是所有的节点在左边都需要小于根节点
'''
class Solution_98:
    def __init__(self):
        self.maxVal = float('-inf')  # 因为后台测试数据中有int最小值

    def isValidBST(self, root):
        if root is None:
            return True

        left = self.isValidBST(root.left)
        # 中序遍历，验证遍历的元素是不是从小到大
        if self.maxVal < root.val:
            self.maxVal = root.val
        else:
            return False
        right = self.isValidBST(root.right)

        return left and right
         
