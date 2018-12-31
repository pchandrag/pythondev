# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0;
        else:
            lDepth = Solution.maxDepth(self,root.left);
            rDepth = Solution.maxDepth(self,root.right);
            return (1+max(lDepth,rDepth));
