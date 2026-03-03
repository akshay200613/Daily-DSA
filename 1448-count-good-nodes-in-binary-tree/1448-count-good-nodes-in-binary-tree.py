# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if not node:
                return 0

            # Check if current node is good
            good = 1 if node.val >= cur_max else 0

            # Update max for children
            new_max = max(cur_max, node.val)

            # Recurse to left and right
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)

            return good

        return dfs(root, root.val)