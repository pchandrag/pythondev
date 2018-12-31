#Single Stack
    def postorderTraversal(self, root):
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
            
            lNode = tmpNode.left;
            rNode = tmpNode.right;
            tmpNode.left = None;
            tmpNode.right= None;
            
            if (lNode is None and rNode is None):
                tmpList.append(tmpNode.val);
            else:
                tmpStack.append(tmpNode);
            
            if (rNode is not None):
                tmpStack.append(rNode);

            if (lNode is not None):
                tmpStack.append(lNode);

        return tmpList;

#Two Stacks
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tmpList =[];
        if root is None:
            return tmpList;

        s1=[];
        s2=[];
        
        s1.append(root);
        while (len(s1)>0):
            tmpNode = s1.pop();
            s2.append(tmpNode);
            if (tmpNode.left is not None):
                s1.append(tmpNode.left);
            if (tmpNode.right is not None): 
                s1.append(tmpNode.right);

        while (len(s2)>0):
            tmpList.append(s2.pop().val);
        return tmpList;
