# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        n = len(preorder)

        def build(lower, upper):
            if self.i ==n:
                return None
            val = preorder[self.i]      
            if val <=lower or val >=upper:
                return None

            self.i += 1
            root = TreeNode(val)
            root.left = build(lower, val)
            root.right = build(val, upper)
            return root
        return build(float("-inf"),float("inf"))  