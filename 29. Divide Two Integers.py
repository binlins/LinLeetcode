#29. Divide Two Integers
# -*- coding:utf-8 -*-
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend : int
        :type divisor: int 
        :rtype: int
        """
        if dividend == 0 or divisor == 0:
            return 0
        count = 0
        tmp = 0   
        absDividend = abs(dividend)  
        absDivisor = abs(divisor)  
        sum = absDivisor  
        while absDividend >= absDivisor:
            tmp = 1   
            sum = absDivisor  
            while sum + sum <= absDividend:
                sum += sum  
                tmp += tmp  
            
            count += tmp  
            absDividend -= sum  
          
        if divisor < 0 and dividend > 0 or divisor > 0 and dividend < 0:  
            count =  -count  
        if count >= 2147483647:
            return 2147483647   
        return count  
         #不是很会这题，看的我吐血
         #思路是 递增，到最后减去超出范围之外最小的数，继续递增