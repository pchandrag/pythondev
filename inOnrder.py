    def inorderTraversal(self, root):
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
            
            if (tmpNode.right is not None):
                tmpStack.append(tmpNode.right);
            
            if (tmpNode.left is not None):
                lNode = tmpNode.left;
                tmpNode.left = None;
                tmpNode.right= None;
                tmpStack.append(tmpNode);  
                tmpStack.append(lNode);
            else:
                tmpList.append(tmpNode.val)
  
        return tmpList;
