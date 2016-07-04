# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if root:
            level = [root]
            while level:
                view += [level[-1].val]
                tmplevel = []
                for node in level:
                    if node.left:
                        tmplevel.append(node.left)
                    if node.right:
                        tmplevel.append(node.right)
                level = tmplevel
        return view
