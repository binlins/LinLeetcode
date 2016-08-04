#69. Sqrt(x)
# -*- coding:utf-8 -*-
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, hig = 0, x
        while low <= hig:
            mid = (hig + low) / 2
            sum = mid * mid
            if sum > x:
                hig = mid - 1
            elif sum < x:
                low = mid + 1
            elif sum == x:
                return mid
            
        return hig
        #机智返回hig