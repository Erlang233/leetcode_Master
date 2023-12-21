#前中后序遍历
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = []
        que.append(root)
        result = []
        while que:
            temp = que.pop()
            result.append(temp.val)
            if temp.right:
                que.append(temp.right)
            if temp.left:
                que.append(temp.left)
            
            
        return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return   left+ [root.val]  + right   

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return   right + left + [root.val]
