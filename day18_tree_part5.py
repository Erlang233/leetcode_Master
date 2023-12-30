# leetcode 513找左下角的值
‘’‘
本题有个思维难点，左下角的值不是从左子树找，而是找最大深度中最靠近左边的值。
其中还蕴涵着回溯这个思想，也是代码随想录中第一次提到回溯。
’‘’
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_depth = -1 # 做一个初始化，把现在最大深度定义为-1
        self.result = None
        self.traversal(root, 0) #这样可以从第一个根节点就开始检测
        return self.result
    
    def traversal(self, node, depth):#每次存在更新，从外面读入一个值，然后有修改操作
        if not node.left and not node.right: 
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return
        
        if node.left: 
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1 #回溯步骤，没有就变成累加了
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1


# leetcode 112
'''
只要验证有一条路径成功
'''

class Solution_112:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



#106 从中序和后序数组中构造树

'''
搞清楚前中后的排列针对的是哪些情况，设置breakp
'''
class Solution_106:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return
        root = TreeNode(postorder[-1])
        breakP = 0 
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                breakP = i
                break
        
        inorder_left = inorder[:breakP]
        inorder_right = inorder[breakP + 1:]

        postorder_left =postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]

        root.left = self.buildTree(inorder_left,postorder_left)
        root.right = self.buildTree(inorder_right,postorder_right)

        return root
