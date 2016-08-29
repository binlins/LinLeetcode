#257. Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:         #I hate these amzing recursive 
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res, path = [], []
        self.bTPR(root, res, path)
        return res
    
    def bTPR(self, node, res, path):
        if node is None:    
            return  
        
        if node.left is node.right is None:
            ans = ''
            for n in path:
                ans += str(n.val) + '->'
            res.append(ans + str(node.val))
            
        if node.left:
            path.append(node)
            self.bTPR(node.left, res, path)
            path.pop()
            
        if node.right:
            path.append(node)
            self.bTPR(node.right, res, path)
            path.pop()