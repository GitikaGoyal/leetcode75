# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = deque([root])

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        levelTraversal = self.levelOrder(root)
        for level in levelTraversal:
            res.append(level[-1])  # last element = rightmost node
        return res


# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.recursionRight(root, 0, res)
        return res

    def recursionRight(self, root, level, res):
        if not root:
            return        
        if len(res) == level:
            res.append(root.val)
        self.recursionRight(root.right, level + 1, res)        
        self.recursionRight(root.left, level + 1, res)
