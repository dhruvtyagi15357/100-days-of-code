class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == int(str(int(str(num)[::-1]))[::-1])