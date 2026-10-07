# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if 0, return 1
        # elif 1, return max(depth, diameter of child) ++++++++
        # else 2, return sum of depths +++++++
        if not root:
            return 0
        elif not (root.left or root.right):
            return 0
        elif root.left and root.right:
            return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.maxDepth(root.left) + self.maxDepth(root.right))
        elif root.left:
            return max(self.maxDepth(root) - 1, self.diameterOfBinaryTree(root.left))
        elif root.right:
            return max(self.maxDepth(root) - 1, self.diameterOfBinaryTree(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not (root.left or root.right):
            return 1
        elif not root.left:
            return self.maxDepth(root.right) + 1
        elif not root.right:
            return self.maxDepth(root.left) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        