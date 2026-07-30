# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        lca = [root]

        def search(root):
            if root is None:
                return 
            lca[0] = root
            if root is p or root is q:
                return 

            elif root.val < q.val and root.val < p.val:
                search(root.right)
            elif root.val > q.val and root.val > p.val:
                search(root.left)

            else:
                return 

        search(root)

        return lca[0]
        