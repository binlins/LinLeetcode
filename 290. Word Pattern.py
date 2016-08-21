#290. Word Pattern
#-*- coding:utf-8 -*-
#做不出来，脑容量有限，感觉是模模糊糊有思路但是写不出来
from itertools import izip
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != self.wordCount(str):
            return False
        w2p, p2w = {}, {}    
        for p, w in izip(pattern, self.wordGenerator(str)):
            if w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                return False
        return True        
        
        
    def wordCount(self, str):
        cnt = 1 if str else 0
        for c in str:
            if c == ' ':
                cnt += 1
        return cnt        
        
    def wordGenerator(self, str):
        w = ''
        for c in str:
            if c != ' ':
                w += c
            else:
                yield w
                w = ''
        yield w        