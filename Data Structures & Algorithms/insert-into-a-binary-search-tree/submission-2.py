# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=root
        def helper(r:TreeNode):
            if val>r.val:
                if r.right is not None:
                    helper(r.right)
                else:
                    r.right=TreeNode(val)
                    return
            else:
                if r.left is not None:
                    helper(r.left)
                else:
                    r.left=TreeNode(val)
                    return
        if temp is None:
            return TreeNode(val)
        helper(temp)
        return root