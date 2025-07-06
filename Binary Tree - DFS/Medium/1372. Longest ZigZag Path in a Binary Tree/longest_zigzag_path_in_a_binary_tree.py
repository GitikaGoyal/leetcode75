# DFS
# T.C.-> O(n)
# S.C.-> O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0  # instance variable initialized here

        self.zigzagSearch(root, True, 0)
        self.zigzagSearch(root, False, 0)

        return self.maxLength

    def zigzagSearch(self, current, moveLeft, length):
        if not current:
            return

        self.maxLength = max(self.maxLength, length)

        if moveLeft:
            self.zigzagSearch(current.left, False, length + 1)
            self.zigzagSearch(current.right, True, 1)
        else:
            self.zigzagSearch(current.left, False, 1)
            self.zigzagSearch(current.right, True, length + 1)
