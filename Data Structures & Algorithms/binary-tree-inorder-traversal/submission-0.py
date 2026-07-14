class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            li.append(node.val)
            traverse(node.right)
        traverse(root)
        return li