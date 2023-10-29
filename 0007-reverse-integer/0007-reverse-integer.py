class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = -1*int(str(x)[:0:-1])
        if (-1*(2**31))-1 <= x <= (2**31)+1:
            return x
        else:
            return 0