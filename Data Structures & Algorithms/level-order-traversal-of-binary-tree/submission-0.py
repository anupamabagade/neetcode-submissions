# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root :
            queue.append(root)
        
        full_tree = []
        level = 0

        while (len(queue) > 0):
            sub_list = []
            for i in range(len(queue)): # All elements in a level
                curr = queue.popleft()
                sub_list.append(curr.val)
                if curr.left :
                    queue.append(curr.left)
                if curr.right :
                    queue.append(curr.right)
            level += 1
            full_tree.append(sub_list)

        return full_tree

                

