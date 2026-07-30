from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            current1 = q1.popleft()
            current2 = q2.popleft()

            if current1 is None and current2 is None:
                continue

            if current1 is None or current2 is None:
                return False

            if current1.val != current2.val:
                return False

            q1.append(current1.left)
            q1.append(current1.right)

            q2.append(current2.left)
            q2.append(current2.right)

        return True
            