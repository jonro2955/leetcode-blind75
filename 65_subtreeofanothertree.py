# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool

        Basic condition:
        For each node in root tree:
            if (node.val==subroot.val) && (node.left==subroot.left) && (node.right==subroot.right):
                return true
        """

        # First create a function isMatch(self, root, subRoot) to check for the basic condition

        # If root is None, return false immediately
        if not root:
            return False

        # Call isMatch() helper to quickly check if the given root and subRoot are a match
        if self.isMatch(root, subRoot): return True

        # If the above doesn't return true, use recursion to recall the same function on the root
        # tree's subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # This recursive helper is created first and then used inside the main function above
    def isMatch(self, root, subRoot):
        if root and subRoot:  # needed because python cannot evaluate attribute 'val' of NoneType
            return root.val == subRoot.val and self.isMatch(root.left,subRoot.left) and self.isMatch(root.right, subRoot.right)
        return root is subRoot  # Needed so that we return true if both are None and false if not.