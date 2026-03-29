# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p is None or q is None:
            return None
        
        temp=root
        while temp is not None:
            if temp.val>p.val and temp.val>q.val:
                temp=temp.left
            elif temp.val<p.val and temp.val<q.val:
                temp=temp.right
            else:
                return temp