#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:49:28 2019

@author: paul
"""

from copy import deepcopy

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        self.ret = []
        ans = []
        INT_MAX = str(2**31-1)
        self.dfs(S, ans, INT_MAX)
        if self.ret:
            return self.ret[0]
        return self.ret
        
    def dfs(self, S, ans, INT_MAX):
        if len(S) == 0 and len(ans)>=3:
            self.ret.append(ans)
            return
            
        for i in range(0, len(S)):
            if (i+1==len(INT_MAX) and S[:i+1]>INT_MAX) or i+1>len(INT_MAX):
                break
                
            if i==0 and S[i]=='0':  
                if len(ans) <= 1 or (ans[-1] == 0 and ans[-2] == 0):
                    ans.append(0)
                    self.dfs(S[i+1:], deepcopy(ans), INT_MAX)
                    ans.pop(-1)
                break  
            
            elif len(ans)<=1:
                ans.append(int(S[:i+1]))
                self.dfs(S[i+1:], deepcopy(ans), INT_MAX)
                ans.pop(-1)
               
            elif ans[-1]+ans[-2] == int(S[:i+1]):
                ans.append(ans[-1]+ans[-2])
                self.dfs(S[i+1:], deepcopy(ans), INT_MAX)
                ans.pop(-1)
            
            elif ans[-1]+ans[-2] < int(S[:i+1]):
                break
                
if __name__ == "__main__":
    sol = Solution()
    S = "01123581321345589"
    print(sol.splitIntoFibonacci(S))           
            
        
                    
                    
                    
                