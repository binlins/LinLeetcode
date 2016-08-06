#205. Isomorphic Strings
#-*- coding:utf-8 -*-
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):    return False
        # dict = {}
        # for i in xrange(len(s)):
        #     if dict.get(s[i]) == t[i]:
        #         pass
        #     elif not dict.get(s[i]) and t[i] not in dict.values():
        #         dict[s[i]] = t[i]    
        #     elif t[i] in dict.values():
        #         return False
        #     elif dict[s[i]] != t[i]:
        #         return False
        # return True    
        if len(s) != len(t):
            return False
        return self.halfIsome(s, t) and self.halfIsome(t, s)
        
    def halfIsome(self, s, t):
        lookup = {}
        for i in xrange(len(s)):
            if not s[i] in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True        
            
            
            