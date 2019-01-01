class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        tmp=list()
        while (i<len(nums)):
            comp=target-nums[i]
            if (comp in tmp):
                return list((tmp.index(comp),i))
            else:
                tmp.append(nums[i])
                i=i+1
