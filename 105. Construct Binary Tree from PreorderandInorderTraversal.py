# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root= TreeNode(preorder[0])

        stack =[root]
        inorder_index=0

        for i in range(1,len(preorder)):

            node= TreeNode(preorder[i])
            parent=stack[-1]

            if parent.val!=inorder[inorder_index]:
                parent.left=node
            else:
                while stack and stack[-1].val==inorder[inorder_index]:
                    parent=stack.pop()
                    inorder_index+=1
                parent.right=node
            stack.append(node)

        return root
        
