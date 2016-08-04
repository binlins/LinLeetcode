#372. Super Pow
# -*- coding:utf-8 -*-
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        if b is None or len(b) == 0:
            return 0
        a = a % 1337
        for i in xrange(len(b)):
            ans = ((self.pow(ans, 10) * pow(a, b[i])) % 1337)
        return ans
    
    def pow(self, a, b):
        if b == 1:
            return a
        if b == 0:
            return 1
        x = pow(a,b/2)
        x = (x*x) % 1337
        if (b&1) == 1:
            x = (x*a) % 1337
        return x
    #参考网上的蛋疼题