#204. Count Primes
#-*- coding:utf-8 -*-
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        is_prime = [True] * n
        num = 0
        for i in xrange(2, n):
            if is_prime[i]:
               num += 1
               for j in xrange(i+i, n, i):
                   is_prime[j] = False
        return num