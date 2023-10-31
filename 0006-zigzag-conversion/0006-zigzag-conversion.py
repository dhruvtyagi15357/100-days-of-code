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

        r,c = 0,0
        flag = False # go down, flag = True # Go up

        for i in s:
            if r == numRows-1:
                flag=True
            elif r == 0:
                flag=False

            if not flag:
                self.append(rows, i, r)
                r+=1
            else:
                self.append(rows, i, r)
                r-=1
        res = ''
        for i in rows:
            for j in i:
                res+=j
        return res

        
        # index = 0
        # step = -1
        # for char in s:
        #     rows[index].append(char)
        #     if index == 0:
        #         step = 1
        #     elif index == numRows - 1:
        #         step = -1
        #     index += step

        # for i in range(numRows):
        #     rows[i] = ''.join(rows[i])
        # return ''.join(rows)
        # i = 0
        # flag = False    #go down, if flag == True, go up


        # for char in s:
        #     rows[i].append(char)

        #     if 