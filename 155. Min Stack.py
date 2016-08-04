#155. Min Stack
#-*- coding:utf-8 -*-

class MinStack(object):
#风骚的stack   minStack存储最小的值      主要是self.比较麻烦，只知道函数要self  list竟然也要
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            self.minStack.append(x)
        
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.minStack) is not 0 and self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()