class Solution(object):
    def findMedian(self,nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        l=len(nums)
        print nums,l,l/2,l%2
        if (l%2==0):
            return (nums[l/2]+nums[l/2-1])/2.0
        else:
            return (nums[l/2])
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1=len(nums1)
        l2=len(nums2)
        tmp=[]
        
        if (l1==0):
            return self.findMedian(nums2)
        if (l2==0):
            return self.findMedian(nums1)
        
        if (nums1[l1-1]<=nums2[0]):
            tmp=nums1 + nums2
            return self.findMedian(tmp)
        
        if (nums2[l2-1]<=nums1[0]):
            tmp=nums2+nums1
            return self.findMedian(tmp)
        
        i=0
        j=0
        while (i<l1 or j<l2):
            if ((i<l1) and (j>=l2 or nums1[i]<=nums2[j])):
                tmp.append(nums1[i])
                i=i+1
            else:
                tmp.append(nums2[j])
                j=j+1
        return self.findMedian(tmp)
