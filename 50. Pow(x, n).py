#50. Pow(x, n)
# -*- coding:utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n < 0:
            return 1.0 / self.myPw(x, -n)
        else:
            return self.myPw(x, n)
        
    def myPw(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            tmp = self.myPw(x, n >> 1)
            return tmp * tmp
        else:
            tmp = self.myPw(x, (n-1) >> 1)
            return tmp * tmp * x 
            #这很二分