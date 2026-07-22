# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        
        level = 0
        right_side = []

        while(len(queue)>0):
            sublist = []
            
            for i in range(len(queue)):
                curr = queue.popleft()
                sublist.append(curr)

                if curr.left :
                    queue.append(curr.left)
                if curr.right :
                    queue.append(curr.right)
            
            level += 1
            right_side.append(sublist[-1].val)
        
        return right_side




