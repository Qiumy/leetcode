# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
# return [1,3,2].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal_re(self, root, inorder):
        if not root:
            return inorder
        inorder = self.inorderTraversal_re(root.left, inorder)
        inorder.append(root.val)
        inorder = self.inorderTraversal_re(root.right, inorder)
        return inorder

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal_re(root, [])
