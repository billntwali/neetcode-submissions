from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def balancedtree(tree1, tree2):
            q1 = deque([tree1])
            q2 = deque([tree2])

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
            return not q1 and not q2 

        
        if subRoot is None:
            return True

        if root is None:
            return False

        queue = deque([root])
        value = subRoot.val
        while queue:
            current = queue.popleft()
            if current.val == value:
                if balancedtree(current, subRoot):
                    return True

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return False
            


        