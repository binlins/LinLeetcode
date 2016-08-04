#144. Binary Tree Preorder Traversal
#-*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     res = []				#递归解决	Recursive 
    #     self.pre(root, res)
    #     return res
        
    # def pre(self, root, res):
    #     if not root:    return []
    #     res.append(root.val)
    #     self.pre(root.left, res)
    #     self.pre(root.right, res)
        if not root:    return []		#非递归	iteratively 迭代
        stack, res = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:  stack.append(node.right)
            if node.left:   stack.append(node.left)
        return res    