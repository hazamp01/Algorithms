# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         dictionary = {'{':'}','[':']','(':')'}
#         res=[]
#         for k in s:
#             for i,j in dictionary.iteritems():
#                 if k == i:
#                     res.append(i)
#
#                 else:
#                     print "False it is"
# a=Solution()
# a.isValid('[]')

OPENING_BRACKETS = {"{", "[", "("}
BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}

def isValid(s):
    stack = []
    for bracket in s:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif not stack:
            return False        # Can't pop from an empty stack
        elif stack.pop() != BRACKETS_MAP[bracket]:
            return False        # Closing the wrong kind of bracket
    return not stack

print isValid('[({}')