#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:53:30 2019

@author: paul
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.count = 0
        self.dfs(s, p)
        return self.count>0
        
    def dfs(self, s, p):
        if len(s)==0 and len(p)==0:
            self.count+=1
            return True
        if len(s)!=0 and len(p)==0:
            return
        if len(s)==0 and p[-1]!='*':
            return
        
        if p[-1]=='*':
            for i in range(len(s)):
                if s[-i-1]==p[-2] or p[-2]=='.':
                    if self.dfs(s[:-i-1], p[:-2]):
                        return True
                else:
                    break
            if self.dfs(s, p[:-2]):
                return True
        elif p[-1]=='.' or p[-1]==s[-1]:
            if self.dfs(s[:-1], p[:-1]):
                return True
            
if __name__ == "__main__":
    sol = Solution()
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
    print(sol.isMatch(s, p)) 