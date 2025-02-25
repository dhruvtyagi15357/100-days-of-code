class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        for i in range(32):
            if 2**i == n:
                return True

        return False