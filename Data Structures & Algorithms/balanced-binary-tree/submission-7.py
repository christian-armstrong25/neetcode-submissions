# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return abs(self.depth(root.left) - self.depth(root.right)) <= 1 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not (root.left or root.right):
            return 1
        elif not root.left:
            if root.right.right or root.right.left:
                return 3
            else:
                return 2
        elif not root.right:
            if root.left.right or root.left.left:
                return 3
            else:
                return 2
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1
        

        