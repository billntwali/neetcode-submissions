# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        temp = TreeNode(val)

        if root is None:
            return temp

        current = root

        while current is not None:

            if current.val > val and current.left is not None:
                current = current.left
            elif current.val < val and current.right is not None:
                current = current.right 
            else:
                break

        if current.val > val:
            current.left = temp

        if current.val < val:
            current.right = temp

        return root

        