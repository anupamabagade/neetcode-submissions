# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root : # If key not found at all
            return None

        def minValue(node):
            cur = node
            while (cur and cur.left):
                cur = cur.left
            return cur


        if key > root.val :
            root.right = self.deleteNode(root.right, key)
        elif key < root.val :            
            root.left = self.deleteNode(root.left, key)
        else: # Delete at current position
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = minValue(root.right) # If the current node is to be deleted 
                # and has children then the min value on the right subtree will be placed
                # in the position of the node
                root.val = minNode.val 
                root.right = self.deleteNode(root.right, minNode.val) # Delete the value moved to the top
        return root