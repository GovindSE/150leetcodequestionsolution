# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue1= deque([p])
        queue2=deque([q])

        while queue1 and queue2:
            lengthoftrav= len(queue1)
            lengthoftrav1= len(queue2)

            for _ in range (lengthoftrav):
                


                node1= queue1.pop()
                node2= queue2.pop()

                if not node1 and not node2:
                 continue
                if not node1 or not node2:
                 return False
                if node1.val!=node2.val:
                 return False
                queue1.append(node1.left)
                queue2.append(node2.left)
                queue1.append(node1.right)
                queue2.append(node2.right) 

        return not queue1 and not queue2
        
