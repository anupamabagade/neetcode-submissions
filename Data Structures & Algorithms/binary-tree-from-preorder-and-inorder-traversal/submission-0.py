# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1st element of preorder is root, then all left subtree, then right
        # 2nd element of preorder is always root of left subtree

        if not preorder or not inorder :
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid+1], inorder[: mid])
        root.right = self.buildTree(preorder[mid+1 :], inorder[mid+1:])

        return root

