# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret=[];
        t1 = l1;
        t2 = l2;
        
        c = 0;
        while ((t1 is not None) or (t2 is not None)):
            i1 = 0 if (t1 is None) else t1.val;
            i2 = 0 if (t2 is None) else t2.val;
            sum = i1+i2+c;
            if (sum>9):
                ret.append(sum % 10);
                c = sum / 10;
            else:
                ret.append(sum);
                c = 0;

            t1 = None if (t1 is None) else t1.next;
            t2 = None if (t2 is None) else t2.next;
            
        if (c>0):
            ret.append(c);
        
        return ret;
