import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x == 0:
            return True
        l = int(math.floor(math.log10(x)))

        end = int(math.pow(10, l))
        start = 10

        for i in range(l,l/2, -1):
            if x % start != x / end:
                return False
            x = x - end * (x / end)
            x = (x - x % start) / 10
            end = end / 100
        return True
        
s = Solution()
print s.isPalindrome(8121118)
        


