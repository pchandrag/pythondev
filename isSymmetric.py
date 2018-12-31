class Solution(object):
    def isMirror(self, left, right):
        """
        :type left: TreeNode
        :type right: TreeNode
        :rtype: bool
        """
        if (left is None and right is None):
            return True;
        
        if (left is not None and right is not None and left.val == right.val):
            return (Solution.isMirror(self,left.left,right.right) and 
                    Solution.isMirror(self,left.right,right.left)
                   )
        else:
            return False;
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root is None):
            return True;
        else:
            return Solution.isMirror(self,root.left,root.right);
        
