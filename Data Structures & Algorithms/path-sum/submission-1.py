# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if not node : # Empty binary tree
                return False
            
            cur_sum += node.val

            if not node.left and not node.right : # Leaf node
                # Check sum
                if cur_sum == targetSum :
                    return True
                else :
                    return False

            # If not at a leaf node, go to left and right children    
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum) # The or makes sure that the True propogates despite any False returns
        
        return dfs(root, 0)
