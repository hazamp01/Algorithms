class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         nums = [2, 7, 11, 15], target = 9
        j = nums[0]
        for i in nums:
            if j+i == target:
                print (i,j)
            else:
                i = i +1
c = Solution()
c.twoSum(nums = [2, 7, 11, 15], target = 13)
