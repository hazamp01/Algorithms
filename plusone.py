Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


# 66. Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = digits[len(digits)-1]+1
        print value
        if len(str(value))>1:
            replace_value= int(str(value)[:1]),int(str(value)[1:2])
            replace_value =list(replace_value)
        else:
            replace_value = [value]
        return digits[:(len(digits)-1)]+replace_value
        
value = Solution()
value.plusOne([1,2,3,3,9])
