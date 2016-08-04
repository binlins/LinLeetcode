#145. Binary Tree Postorder Traversal
#-*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     res = []
    #     self.post(root, res)
    #     return res
        
    # def post(self, root, res):    
    #     if not root:    return []
    #     self.post(root.left, res)
    #     self.post(root.right, res)
    #     res.append(root.val)
        stack, res = [], []
        mark, node = None, root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right is mark:#防止无限循环right
                res.append(node.val)
                mark = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return res        