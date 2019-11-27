# Defanged version of IP address

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        for i in address:
            if i==".":
                i.replace(".","[.]")
        return address
res = Solution()
res.defangIPaddr("1.1.1.1")
