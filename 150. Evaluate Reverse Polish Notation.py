#150. Evaluate Reverse Polish Notation
#-*- coding:utf-8 -*-
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num = []
        oper = ['+', '-', '*', '/']
        for x in tokens:
            if x not in oper:
                num.append(int(x))
            else:
                i = num.pop()
                j = num.pop()
                if x == '+':    num.append(j + i)
                if x == '-':    num.append(j - i)
                if x == '*':    num.append(j * i)
                if x == '/':
                    num.append(int(j*1.0 / i))
        return num.pop()
                
                