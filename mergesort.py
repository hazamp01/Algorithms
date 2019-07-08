class Solution(object):
    def removeElement(self, nums, val):
       for i in nums:
           if nums[i]==val:
               nums.remove(i)

a=Solution()
a.removeElement([0,1,2,2,3, 0,4,2], 2)