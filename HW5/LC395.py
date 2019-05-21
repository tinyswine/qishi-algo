#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:34:11 2019

@author: paul
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if len(s)==0:
            return 0
        
        count_dict = {}
        index_dict = {}
        for i in range(len(s)):
            c = s[i]
            count_dict[c] = count_dict.get(c,0)+1
            index_dict[c] = i
        
        for c in count_dict:
            if count_dict[c]<k:
                s1, s2 = s[:index_dict[c]], s[index_dict[c]+1:]
                return max(self.longestSubstring(s1, k), self.longestSubstring(s2, k))
        return len(s)
    
if __name__ == "__main__":
    s = "aaabb"
    k = 3
    sol = Solution()
    print(sol.longestSubstring(s, k))