class Solution(object):
    def append(self, arr, element, row):
        arr[row].append(element)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if numRows == 1 or numRows > l:
            return s
        
        rows = [[] for row in range(numRows)]
        r = 0
        flag = False # go down, flag = True # Go up

        for i in s:
            if r == numRows-1:
                flag=True
            elif r == 0:
                flag=False

            self.append(rows, i, r)
            if not flag:
                r+=1
            else:
                r-=1
        res = ''
        for i in rows:
            for j in i:
                res+=j
        return res