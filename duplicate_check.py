class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_=0
        if len(nums)>1:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]==nums[j]:
                        len_=len_+1
            if len_>0:
                return True
            else:
                return False
        else:
            return False
            
value = Solution()
value.containsDuplicate([1,2,3,1])
