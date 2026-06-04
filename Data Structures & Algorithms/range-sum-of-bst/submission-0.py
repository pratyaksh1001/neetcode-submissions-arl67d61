class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        res = 0
        q = [root]

        while q:
            curr = q.pop(0)

            if low <= curr.val <= high:
                res += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            elif curr.val < low:
                # Left subtree values are even smaller, so skip it
                if curr.right:
                    q.append(curr.right)

            else:  # curr.val > high
                # Right subtree values are even larger, so skip it
                if curr.left:
                    q.append(curr.left)

        return res