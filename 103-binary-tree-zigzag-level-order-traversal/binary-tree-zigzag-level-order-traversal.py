# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        q = deque()
        q.append(root)
        n = 0

        while q:
            level = []
            n += 1 
            
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level and n % 2 == 0:  
                level.reverse()
                arr.append(level)
            elif level:
                arr.append(level)
        
        return arr