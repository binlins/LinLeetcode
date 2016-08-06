#20. Valid Parentheses
#-*- coding:utf-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, dic = [], {'(': ')', '[': ']', '{': '}'}
        for x in s:
            if x in dic:
                stack.append(x)
            elif len(stack) == 0 or dic[stack.pop()] != x:
                return False
        return len(stack) == 0        