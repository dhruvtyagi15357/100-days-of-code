class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s = 0
        for i in range(m,n+1, m):
            s += i
        return sum(range(1,n+1))-(2*s)