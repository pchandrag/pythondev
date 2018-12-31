# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if (root is None):
            return False;
        elif (root.left is None and root.right is None and sum==root.val):
            return True;
        else:
            return(Solution.hasPathSum(self,root.left ,sum-root.val) or
                   Solution.hasPathSum(self,root.right,sum-root.val)
                  )
        
