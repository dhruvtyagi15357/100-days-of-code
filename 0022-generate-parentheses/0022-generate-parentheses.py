class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        def backtrack(o,c, path):
            if o == c == n:
                res.append(path)
                return

            if o < n:
                backtrack(o+1, c, path+'(')
            if c < o:
                backtrack(o, c+1, path+')')
        
        backtrack(0, 0, "")
        return res