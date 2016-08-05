#331. Verify Preorder Serialization of a Binary Tree
#-*- coding:utf-8 -*-
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #将元素压入栈
        #如果当前栈的深度≥3，并且最顶端两个元素为'#', '#'，而第三个元素不为'#'，则将这三个元素弹出栈顶，然后向栈中压入一个'#'，重复此过程
        #最后判断栈中剩余元素是否只有一个'#'
        # if not preorder:    return False      #慢
        # stack = []
        # i = 0
        # pre = preorder.split(',')
        # print pre
        # while i < len(pre):
        #     stack.append(pre[i])
        #     while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and not stack[-3] == '#':
        #         stack.pop() 
        #         stack.pop() 
        #         stack.pop() 
        #         stack.append('#')
        #     i += 1
        # #return stack
        # return len(stack) == 1 and stack[0] == '#'
        
        # stack = []              #快    
        # for item in preorder.split(','):
        #     stack.append(item)
        #     while len(stack) >= 3 and \
        #           stack[-1] == stack[-2] == '#' and \
        #           stack[-3] != '#':
        #         stack.pop(), stack.pop(), stack.pop()
        #         stack.append('#')
        # #return stack        
        # return len(stack) == 1 and stack[0] == '#'
        #统计树的出度（out-degree）和入度（in-degree）
        diff = 1
        for item in preorder.split(','):
            diff -=1
            if diff < 0: return False
            if item != '#': diff += 2
        return diff == 0