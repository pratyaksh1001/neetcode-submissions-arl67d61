# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        q.append(root)
        r=[]
        if root is None:
            return []
        while len(q)>0:
            size=len(q)
            t=[]
            for i in range(size):
                curr=q.popleft()
                t.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            r.append(t[-1])
        return r