class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth_measure(root):
            if not root:
                return 0
            return 1 + max(depth_measure(root.left), depth_measure(root.right))

        left_height = depth_measure(root.left)
        right_height = depth_measure(root.right)
            
        if abs(left_height - right_height) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False