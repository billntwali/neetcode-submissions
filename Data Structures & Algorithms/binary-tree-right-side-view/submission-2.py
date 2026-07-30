from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        result = []

        queue = deque([root])

        while queue:
            value = queue[-1].val
            result.append(value)
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

        return result

        