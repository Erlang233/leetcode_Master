# 235 二叉搜索树的最近公共祖先
'''
可以借鉴搜索树的性质
'''

class Solution:
    def traversal(self, cur, p, q):
        if cur is None:
            return cur
                                                        # 中
        if cur.val > p.val and cur.val > q.val:           # 左
            left = self.traversal(cur.left, p, q)
            if left is not None:
                return left

        if cur.val < p.val and cur.val < q.val:           # 右
            right = self.traversal(cur.right, p, q)
            if right is not None:
                return right

        return cur

    def lowestCommonAncestor(self, root, p, q):
        return self.traversal(root, p, q)


# 701 二叉搜索树中的插入操作
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, return a new node with the value
        if not root:
            return TreeNode(val)

        # Find the position to insert the new node
        pos = self.travel(root, val)
        valNode = TreeNode(val)

        # Insert the node
        if pos.val > val:
            pos.left = valNode
        else:
            pos.right = valNode
        
        return root


    def travel(self, root, val):
    # Base case: if the current node is a leaf node
        if not root.left and root.val > val:
            return root
        if not root.right and root.val < val:
            return root

        # Recursive case: navigate left or right
        if root.val > val and root.left:
            return self.travel(root.left, val)
        elif root.val < val and root.right:
            return self.travel(root.right, val)
        else:
            return root


# 二叉搜索树中删除节点
            

class Solution:
    def deleteNode(self, root, key):
        if root is None:  # 如果根节点为空，直接返回
            return root
        if root.val == key:  # 找到要删除的节点
            if root.right is None:  # 如果右子树为空，直接返回左子树作为新的根节点
                return root.left
            cur = root.right
            while cur.left:  # 找到右子树中的最左节点
                cur = cur.left
            root.val, cur.val = cur.val, root.val  # 将要删除的节点值与最左节点值交换
        root.left = self.deleteNode(root.left, key)  # 在左子树中递归删除目标节点
        root.right = self.deleteNode(root.right, key)  # 在右子树中递归删除目标节点
        return root
          
