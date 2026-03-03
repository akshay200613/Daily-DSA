# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque()
        # store (node, max_value_on_path_to_this_node)
        q.append((root, root.val))
        count = 0

        while q:
            node, cur_max = q.popleft()

            if node.val >= cur_max:
                count += 1

            new_max = max(cur_max, node.val)

            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))

        return count