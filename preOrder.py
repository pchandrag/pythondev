    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tmpList =[];
        if root is None:
            return tmpList;
        
        tmpStack=[];
        tmpStack.append(root);
        while (len(tmpStack)>0):
            tmpNode = tmpStack.pop();
            tmpList.append(tmpNode.val);
            
            if (tmpNode.right is not None):
                tmpStack.append(tmpNode.right);
            if (tmpNode.left is not None):
                tmpStack.append(tmpNode.left);
        return tmpList;
