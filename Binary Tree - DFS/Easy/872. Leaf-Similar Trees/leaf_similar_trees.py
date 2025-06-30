#Approach - DFS
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2


#Approach - DFS (Space Optimized)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            dfs(root.left, leaf)
            dfs(root.right, leaf)
        
        leaf1 = []
        dfs(root1, leaf1)

        def dfs1(root, leaf):
            if not root:
                return True
            if not root.left and not root.right:
                if not leaf:
                    return False
                return leaf.pop() == root.val            
            return dfs1(root.right, leaf) and dfs1(root.left, leaf)
        
        return dfs1(root2, leaf1) and not leaf1

#Approach - Iterative DFS
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getPathLeaf(stack):
            while stack:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if not node.left and not node.right:
                    return node.val

        stack1, stack2 = [root1], [root2]
        while stack1 and stack2:
            if getPathLeaf(stack1) != getPathLeaf(stack2):
                return False
        
        return not stack1 and not stack2
