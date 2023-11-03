# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = 0
        def trav(root):

            nonlocal res  
            
            if root == None:
                return (0,0)

            left = trav(root.left)
            right = trav(root.right)

            ts= left[0] + right[0] + root.val
            tc=left[1]+ right[1] + 1

            if root.val == (ts//tc):
                res += 1
                
            return (ts,tc)


        trav(root)

        return res