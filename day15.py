#LC102,107,199,637,429,515,116,117,104,111,226
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = collections.deque([root])
        result = []
        
        while que:
            level = []
            for _ in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
            result.append(level)
        
        return result

  class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        
        que = collections.deque([root])
        result = []

        while que:
            layer = []
            for _ in range(len(que)):
                cur = que.popleft()
                layer.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
            result.append(layer)

        return result[::-1]


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        
        que = collections.deque([root])
        result = []
        
        while que:
            level_size = len(que)
            for i in range(level_size):
                cur = que.popleft()

                if i == level_size-1:
                    print(cur.val)
                    result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                
        
        return result


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        que = collections.deque([root])
        result = []

        while que:
            level_sum = 0 
            count = 0
            for _ in range (len(que)):
                cur = que.popleft()
                level_sum += cur.val
                count += 1
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            result.append(level_sum/count)
        return result


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = collections.deque([root])
        result = []

        while que:
            level = [] 
            for _ in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                for tree in cur.children:
                    que.append(tree)
            result.append(level)
        
        return result


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        que = collections.deque([root])
        result = [] 

        while que:
            level = []
            for _ in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            result.append(max(level))
        
        return result


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        que = collections.deque([root])
        
        while que:
            level_size = len(que)
            pre = None 
            for i in range(level_size):
                cur = que.popleft()
                if pre:
                    pre.next = cur
                pre = cur 

                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
        
        return root    


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = collections.deque([root])
        count = 0
        
        while que:
            count += 1 
            level_size = len(que)
            for i in range (level_size):
                cur= que.popleft()
                
                
                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
            
        return count 


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = collections.deque([root])
        count = 0
        
        while que:
            count += 1 
            level_size = len(que)
            for i in range (level_size):
                cur= que.popleft()
                
                
                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
                
                if not cur.left and not cur.right:
                    return count
            
        return count 


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)


        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)


        return root

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        #首先排除空节点的情况
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        #排除了空节点，再排除数值不相同的情况
        elif left.val != right.val: return False
        
        #此时就是：左右节点都不为空，且数值相同的情况
        #此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right) #左子树：左、 右子树：右
        inside = self.compare(left.right, right.left) #左子树：右、 右子树：左
        isSame = outside and inside #左子树：中、 右子树：中 （逻辑处理）
        return isSame



