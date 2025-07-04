#Approach: Brute-Force
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (
            self.dfs(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )

    def dfs(self, node: TreeNode, targetSum: int) -> int:
        if not node:
            return 0
        return (
            (1 if node.val == targetSum else 0)
            + self.dfs(node.left, targetSum - node.val)
            + self.dfs(node.right, targetSum - node.val)
        )



#Approach: Hash Map
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case

        return self.dfs(root, 0, targetSum, prefix_sum_count)

    def dfs(self, node, curr_sum, target, prefix_sum_count):
        if not node:
            return 0

        curr_sum += node.val
        num_paths = prefix_sum_count[curr_sum - target]

        # Add current prefix sum to map
        prefix_sum_count[curr_sum] += 1

        # Recurse into left and right subtrees
        left = self.dfs(node.left, curr_sum, target, prefix_sum_count)
        right = self.dfs(node.right, curr_sum, target, prefix_sum_count)

        # Backtrack
        prefix_sum_count[curr_sum] -= 1

        return num_paths + left + right
