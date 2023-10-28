# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def solve(root):
            if root == None:
                return

            ans.append(root.val)
            solve(root.left)
            solve(root.right)

        solve(root)
        return ans