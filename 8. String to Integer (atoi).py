class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign, base, i = 1, 0, 0
        if len(str) == 0:return 0
        while str[i] == ' ': 
            i += 1
        
        if str[i] == '-' or str[i] == '+':
            sign = 1 - 2 * (str[i] == '-')
            i += 1
            
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            base = base * 10 + (ord(str[i]) - ord('0'))
            i += 1
        res = base*sign    
        if res >= 2147483648:   res = 2147483647       #用以适配C的最值问题
        elif res <= -2147483648: res = -2147483648
        return res