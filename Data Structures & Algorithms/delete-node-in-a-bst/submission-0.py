# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # I need to find that node

        parent = None
        current = root

        while current is not None and current.val != key:
            parent = current

            if current.val < key:
                current = current.right
            else:
                current = current.left

        # Now current is pointing to the value we want or the key we want to remove

        # The next move is to find it's successor we llok for it in the right subtree

        if current is None:
            return root

        if current.left is not None and current.right is not None:
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left 

            current.val = successor.val # Now we put the successor in the current value which is also the one we want to delete
            parent = successor_parent
            current = successor 

        if current.left is not None:
            child = current.left

        else:
            child = current.right

        if parent is None:
            return child

        if parent.left is current:
            parent.left = child

        else:
            parent.right = child

        return root